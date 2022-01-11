"""
Until https://github.com/SeleniumHQ/selenium/issues/9917 is resolved,
combine the upstream wheel which includes bazel-generated files
and the source distribution which has the rest of the metadata for a legacy install.
"""
import os
from pathlib import Path
import shutil

SRC_DIR = Path(os.environ["SRC_DIR"])

SRC = SRC_DIR / "src/py/selenium"
DIST = SRC_DIR / "dist/selenium"


for src in sorted(DIST.rglob("*")):
    if src.is_dir():
        continue
    dest = SRC / src.relative_to(DIST)
    if dest.exists():
        continue
    if not dest.parent.exists():
        dest.mkdir(parents=True)
    print(
        f"---- {src}",
        "\n",
        f" -> {dest}"
    )
    shutil.copy2(src, dest)
