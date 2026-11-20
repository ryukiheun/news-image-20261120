#!/usr/bin/env python3
"""Put the pre-drawn front page at /output/entry.png.

The picture is drawn ahead of time by render.py and committed next to
this file as entry.png, because the grading sandbox has no network and
installs nothing. This program only copies bytes, so two runs always
write the same file.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(target_dir, "entry.png"))


if __name__ == "__main__":
    main()
