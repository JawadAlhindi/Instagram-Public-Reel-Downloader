#!/usr/bin/env python3
"""
Instagram Public Reel Downloader

Downloads public Instagram Reels at highest available resolution using yt-dlp.
No login, no cookies, no watermark, no re-encoding.
"""

__version__ = "1.0.0"

import argparse
import os
import subprocess
import sys
import re


def get_ytdlp_path() -> str:
    """Find yt-dlp executable - check local folder first, then PATH."""
    # Get the directory where this script/exe is located
    if getattr(sys, 'frozen', False):
        # Running as compiled exe
        script_dir = os.path.dirname(sys.executable)
    else:
        # Running as script
        script_dir = os.path.dirname(os.path.abspath(__file__))

    # Check for yt-dlp.exe in same folder (Windows)
    local_ytdlp = os.path.join(script_dir, "yt-dlp.exe")
    if os.path.isfile(local_ytdlp):
        return local_ytdlp

    # Check for yt-dlp (no extension) in same folder (Linux/Mac)
    local_ytdlp = os.path.join(script_dir, "yt-dlp")
    if os.path.isfile(local_ytdlp):
        return local_ytdlp

    # Fall back to PATH
    return "yt-dlp"


def is_valid_instagram_reel_url(url: str) -> bool:
    """Validate that the URL is an Instagram Reel URL."""
    patterns = [
        r'^https?://(www\.)?instagram\.com/reel/[\w-]+/?',
        r'^https?://(www\.)?instagram\.com/reels/[\w-]+/?',
        r'^https?://(www\.)?instagram\.com/p/[\w-]+/?',
    ]
    return any(re.match(pattern, url) for pattern in patterns)


def download_reel(url: str, output: str | None = None, quiet: bool = False) -> int:
    """
    Download an Instagram Reel using yt-dlp.

    Args:
        url: Instagram Reel URL
        output: Output filename (optional)
        quiet: Suppress progress output

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    ytdlp = get_ytdlp_path()

    cmd = [
        ytdlp,
        "-f", "bv*+ba/b",
        "--merge-output-format", "mp4",
    ]

    if output:
        cmd.extend(["-o", output])

    if quiet:
        cmd.append("--quiet")

    cmd.append(url)

    try:
        result = subprocess.run(cmd, check=False)
        return result.returncode
    except FileNotFoundError:
        print("Error: yt-dlp not found!", file=sys.stderr)
        print()
        print("Solutions:", file=sys.stderr)
        print("  1. Download yt-dlp.exe from: https://github.com/yt-dlp/yt-dlp/releases", file=sys.stderr)
        print("     and place it in the same folder as this program", file=sys.stderr)
        print("  2. Or install via pip: pip install yt-dlp", file=sys.stderr)
        print()
        input("Press Enter to exit...")
        return 1


def interactive_mode() -> int:
    """Run in interactive mode - prompt user for URL."""
    print("=" * 50)
    print(f"  Instagram Public Reel Downloader v{__version__}")
    print("=" * 50)
    print()

    while True:
        url = input("Paste Instagram Reel URL (or 'q' to quit): ").strip()

        if url.lower() == 'q':
            print("Goodbye!")
            return 0

        if not url:
            print("No URL entered. Try again.\n")
            continue

        if not is_valid_instagram_reel_url(url):
            print("Invalid Instagram Reel URL. Try again.\n")
            continue

        print("\nDownloading...\n")
        result = download_reel(url)

        if result == 0:
            print("\nDownload complete!")
        else:
            print("\nDownload failed.")

        print()


def pause_before_exit():
    """Pause before closing (for double-click users)."""
    print()
    input("Press Enter to exit...")


def main() -> int:
    # If no arguments, run interactive mode
    if len(sys.argv) == 1:
        try:
            return interactive_mode()
        except KeyboardInterrupt:
            print("\nCancelled.")
            return 0
        except Exception as e:
            print(f"\nError: {e}", file=sys.stderr)
            pause_before_exit()
            return 1

    parser = argparse.ArgumentParser(
        description="Download public Instagram Reels at highest quality.",
        epilog="Example: %(prog)s https://www.instagram.com/reel/ABC123/"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "url",
        nargs="?",
        help="Instagram Reel URL to download"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output filename (default: yt-dlp default naming)"
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress progress output"
    )

    args = parser.parse_args()

    if not args.url:
        return interactive_mode()

    # Validate URL
    if not is_valid_instagram_reel_url(args.url):
        print(f"Error: Invalid Instagram Reel URL: {args.url}", file=sys.stderr)
        print("URL should be in format: https://www.instagram.com/reel/<id>/", file=sys.stderr)
        return 1

    return download_reel(args.url, args.output, args.quiet)


if __name__ == "__main__":
    sys.exit(main())
