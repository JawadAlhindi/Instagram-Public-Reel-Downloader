#!/usr/bin/env python3
"""Build script to create standalone executable."""

import subprocess
import sys


def main():
    """Build the executable using PyInstaller."""
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--console",
        "--name", "ReelDownloader",
        "--icon", "NONE",
        "reel_downloader.py"
    ]

    print("Building executable...")
    result = subprocess.run(cmd, check=False)

    if result.returncode == 0:
        print("\nBuild complete!")
        print("Executable location: dist/ReelDownloader.exe")
    else:
        print("\nBuild failed!")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
