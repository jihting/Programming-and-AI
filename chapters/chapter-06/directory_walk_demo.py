"""Week 2 Lab 2 support file: simple recursive directory walk.

Run this in a small folder. Do not point it at your whole home directory.
"""

from pathlib import Path


def walk_folder(folder, depth=0, max_depth=2, pattern=None):
    """Print files inside folder and recursively inspect subfolders."""
    folder = Path(folder)

    if depth > max_depth:
        return

    indent = "  " * depth
    print(f"{indent}[{folder.name}]")

    for item in sorted(folder.iterdir()):
        if item.is_file():
            if pattern is None or item.name.endswith(pattern):
                print(f"{indent}  {item.name}")
        elif item.is_dir():
            walk_folder(item, depth + 1, max_depth, pattern)


if __name__ == "__main__":
    walk_folder(".", max_depth=2)
    # Try changing max_depth to 3.
    # Try adding pattern=".py".
