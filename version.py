#!/usr/bin/env python3
"""Version management script - updates version and creates git tag."""

import re
import subprocess
import sys

VERSION_FILE = "reel_downloader.py"


def get_current_version() -> str:
    """Read current version from source file."""
    with open(VERSION_FILE, "r") as f:
        content = f.read()
    match = re.search(r'__version__\s*=\s*"([^"]+)"', content)
    return match.group(1) if match else "0.0.0"


def set_version(new_version: str) -> None:
    """Update version in source file."""
    with open(VERSION_FILE, "r") as f:
        content = f.read()

    content = re.sub(
        r'__version__\s*=\s*"[^"]+"',
        f'__version__ = "{new_version}"',
        content
    )

    with open(VERSION_FILE, "w") as f:
        f.write(content)


def main():
    current = get_current_version()
    print(f"Current version: {current}")

    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python version.py 1.2.0        Set version to 1.2.0")
        print("  python version.py patch        Bump patch (1.0.0 -> 1.0.1)")
        print("  python version.py minor        Bump minor (1.0.0 -> 1.1.0)")
        print("  python version.py major        Bump major (1.0.0 -> 2.0.0)")
        return 0

    arg = sys.argv[1]
    parts = current.split(".")
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])

    if arg == "patch":
        new_version = f"{major}.{minor}.{patch + 1}"
    elif arg == "minor":
        new_version = f"{major}.{minor + 1}.0"
    elif arg == "major":
        new_version = f"{major + 1}.0.0"
    else:
        new_version = arg

    print(f"New version: {new_version}")

    # Update file
    set_version(new_version)
    print(f"Updated {VERSION_FILE}")

    # Ask to create git tag
    response = input("\nCreate git commit and tag? (y/n): ").strip().lower()
    if response == "y":
        subprocess.run(["git", "add", VERSION_FILE], check=True)
        subprocess.run(["git", "commit", "-m", f"Bump version to {new_version}"], check=True)
        subprocess.run(["git", "tag", f"v{new_version}"], check=True)
        print(f"\nCreated tag v{new_version}")
        print(f"Run: git push && git push origin v{new_version}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
