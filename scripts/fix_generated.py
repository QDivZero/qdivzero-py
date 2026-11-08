"""Repair missing Unset imports emitted by openapi-python-client 0.29.0."""

import ast
import sys
from pathlib import Path


def main(package: Path) -> None:
    for path in package.rglob("*.py"):
        content = path.read_text()
        if "Unset" not in content:
            continue
        tree = ast.parse(content)
        if any(isinstance(node, ast.ClassDef) and node.name == "Unset" for node in tree.body):
            continue
        if not any(isinstance(node, ast.Name) and node.id == "Unset" for node in ast.walk(tree)):
            continue
        imports = [
            node for node in tree.body if isinstance(node, ast.ImportFrom) and node.module == "types" and node.level
        ]
        if any(alias.name == "Unset" for node in imports for alias in node.names):
            continue
        if not imports:
            raise RuntimeError(f"cannot locate generated types import in {path}")
        node = imports[-1]
        lines = content.splitlines(keepends=True)
        lines.insert(node.end_lineno, f"from {'.' * node.level}types import Unset\n")
        path.write_text("".join(lines))


if __name__ == "__main__":
    main(Path(sys.argv[1]))
