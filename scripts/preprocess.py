"""Make untyped OpenAPI request bodies usable by openapi-python-client."""

import json
import sys
from pathlib import Path


def main(source: Path, output: Path) -> None:
    spec = json.loads(source.read_text())
    methods = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
    for item in spec.get("paths", {}).values():
        for method, operation in item.items():
            if method not in methods or not isinstance(operation, dict):
                continue
            for media in operation.get("requestBody", {}).get("content", {}).values():
                media.setdefault("schema", {})
    output.write_text(json.dumps(spec))


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
