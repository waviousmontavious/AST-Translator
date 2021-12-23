import ast
from pathlib import Path


def get_tree_from_file(path) -> ast.Module:
    with Path(path).open(mode='r', encoding='utf8') as f:
        return ast.parse(f.read())