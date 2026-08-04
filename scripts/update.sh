#!/usr/bin/env bash
# Regenerates the qdivzero-py client from the live OpenAPI spec and publishes
# a new v1.0.<n> tag when the spec changed. Runs locally or in CI.
set -euo pipefail
cd "$(dirname "$0")/.."

SPEC_URL="${SPEC_URL:-https://api.qdiv0.com/openapi}"
OPC_VERSION="${OPC_VERSION:-0.29.0}"

RAW="$(mktemp)"
trap 'rm -f "$RAW"' EXIT

echo "==> fetching spec: $SPEC_URL"
curl -fsSL "$SPEC_URL" -o "$RAW"

if cmp -s "$RAW" api/openapi.json; then
  echo "==> spec unchanged, nothing to do"
  exit 0
fi

export PATH="$HOME/.local/bin:$PATH"
if ! command -v openapi-python-client >/dev/null 2>&1; then
  echo "==> installing openapi-python-client $OPC_VERSION"
  uv tool install "openapi-python-client==$OPC_VERSION"
fi
if ! command -v ruff >/dev/null 2>&1; then
  uv tool install ruff
fi

LATEST="$(git tag --sort=-v:refname | grep '^v1\.0\.' | head -n1 || true)"
if [ -z "$LATEST" ]; then
  NEXT="v1.0.1"
else
  BASE="${LATEST#v}"
  REST="${BASE#*.}"
  PATCH="${REST#*.}"
  NEXT="v1.0.$((PATCH + 1))"
fi

echo "==> regenerating client for $NEXT"
python3 - "${NEXT#v}" <<'EOF'
import sys
path = "api/opc-config.yaml"
with open(path) as f:
    content = f.read()
lines = []
for line in content.splitlines():
    if line.startswith("package_version_override:"):
        lines.append(f'package_version_override: "{sys.argv[1]}"')
    else:
        lines.append(line)
with open(path, "w") as f:
    f.write("\n".join(lines) + "\n")
EOF
openapi-python-client generate --path "$RAW" --config api/opc-config.yaml --meta uv --output-path . --overwrite

echo "==> restoring hand-written files"
cp scripts/wrapper/__init__.py qdivzero_py/__init__.py
cp scripts/wrapper/auth.py qdivzero_py/auth.py
git checkout -- README.md .gitignore

python3 - <<'EOF'
path = "pyproject.toml"
content = open(path).read()
if "[dependency-groups]" not in content:
    with open(path, "a") as f:
        f.write("\n[dependency-groups]\ndev = [\n    \"pytest>=9.1.1\",\n]\n")
EOF

echo "==> verifying"
uv sync
uv run ruff check qdivzero_py tests examples --fix --unsafe-fixes
uv run ruff check qdivzero_py tests examples
uv run pytest

HASH="$(python3 -c 'import hashlib,sys; print(hashlib.sha256(open(sys.argv[1],"rb").read()).hexdigest()[:12])' "$RAW")"

echo "==> committing and tagging $NEXT"
cp "$RAW" api/openapi.json
git config user.name "${GIT_AUTHOR_NAME:-github-actions[bot]}"
git config user.email "${GIT_AUTHOR_EMAIL:-41898282+github-actions[bot]@users.noreply.github.com}"
git add api/openapi.json api/opc-config.yaml pyproject.toml uv.lock qdivzero_py tests
git commit -m "chore: regenerate from OpenAPI spec (hash $HASH)"
git push origin "HEAD:main"
git tag "$NEXT"
git push origin "$NEXT"
echo "==> released $NEXT"
