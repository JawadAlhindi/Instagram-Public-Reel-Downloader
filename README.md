# Instagram Public Reel Downloader

[![Release](https://img.shields.io/github/v/release/JawadAlhindi/Instagram-Public-Reel-Downloader)](https://github.com/JawadAlhindi/Instagram-Public-Reel-Downloader/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/github/downloads/JawadAlhindi/Instagram-Public-Reel-Downloader/total)](https://github.com/JawadAlhindi/Instagram-Public-Reel-Downloader/releases)

A minimal, reliable tool to download **public Instagram Reels** at the highest available resolution.

## Features

- Downloads public Instagram Reels at maximum quality (up to 1080x1920)
- No login or authentication required
- No cookies needed
- No watermark on downloaded videos
- No re-encoding (original quality preserved)
- MP4 output format
- Progress display
- URL validation
- Clear error messages
- Interactive mode (double-click to run)

## Download

**[⬇️ Download Latest Release](https://github.com/JawadAlhindi/Instagram-Public-Reel-Downloader/releases/latest)**

### Quick Start

1. Download `ReelDownloader-Windows.zip` from the [Releases](https://github.com/JawadAlhindi/Instagram-Public-Reel-Downloader/releases/latest) page
2. Extract the ZIP file
3. Double-click `ReelDownloader.exe`
4. Paste your Instagram Reel URL and press Enter

That's it! No Python or technical knowledge required.

## Requirements (For Developers)

- Python 3.10+
- yt-dlp

## Installation (From Source)

1. Clone the repository:
```bash
git clone https://github.com/JawadAlhindi/Instagram-Public-Reel-Downloader.git
cd Instagram-Public-Reel-Downloader
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Building the Executable

To build the standalone `.exe` file:

```bash
python build.py
```

The executable will be created at `dist/ReelDownloader.exe`

## Releasing New Versions

Use the version script to manage releases:

```bash
# See current version
python version.py

# Bump patch version: 1.0.0 → 1.0.1 (bug fixes)
python version.py patch

# Bump minor version: 1.0.0 → 1.1.0 (new features)
python version.py minor

# Bump major version: 1.0.0 → 2.0.0 (breaking changes)
python version.py major

# Set specific version
python version.py 2.5.0
```

The script will update the version and optionally create a git commit and tag.

After running the script, push to GitHub to trigger the release:

```bash
git push && git push origin v1.1.0
```

GitHub Actions will automatically build the executable and create a release.

## Usage

### Interactive Mode (Double-Click)

Simply double-click `reel_downloader.py` to launch interactive mode:

```
==================================================
  Instagram Public Reel Downloader
==================================================

Paste Instagram Reel URL (or 'q' to quit):
```

Paste your URL and press Enter. Download multiple reels in one session!

### Command Line Usage

```bash
python reel_downloader.py <REEL_URL>
```

### Examples

Download a reel:
```bash
python reel_downloader.py https://www.instagram.com/reel/ABC123/
```

Download with custom filename:
```bash
python reel_downloader.py -o my_video.mp4 https://www.instagram.com/reel/ABC123/
```

Download in quiet mode (no progress output):
```bash
python reel_downloader.py -q https://www.instagram.com/reel/ABC123/
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `url` | Instagram Reel URL (required) |
| `-o, --output` | Output filename |
| `-q, --quiet` | Suppress progress output |
| `-h, --help` | Show help message |

### Supported URL Formats

- `https://www.instagram.com/reel/<id>/`
- `https://instagram.com/reel/<id>/`
- `https://www.instagram.com/reels/<id>/`
- `https://www.instagram.com/p/<id>/`

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | Error (invalid URL, download failed, yt-dlp not installed) |

## Limitations

- Only works with **public** reels
- Maximum quality is limited by Instagram (typically 1080x1920)
- Private reels are not supported

## Troubleshooting

### yt-dlp not found
```
Error: yt-dlp not found!
```
**For EXE users:** Make sure `yt-dlp.exe` is in the same folder as `ReelDownloader.exe`. If missing, download it from [yt-dlp releases](https://github.com/yt-dlp/yt-dlp/releases/latest).

**For Python users:** Install with `pip install yt-dlp`

### Invalid URL
```
Error: Invalid Instagram Reel URL
```
Solution: Make sure the URL is a valid Instagram Reel URL in the supported format.

### Download fails
Instagram may rate-limit requests. Wait a few minutes and try again.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for personal use only. Respect Instagram's Terms of Service and content creators' rights. Only download content you have permission to download.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The powerful media downloader that powers this tool
