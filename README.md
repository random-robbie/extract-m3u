# IPTV M3U Credential Extractor

A Python tool to extract usernames and passwords from IPTV M3U playlist URLs for security testing and analysis purposes.

## Description

This tool parses IPTV URLs that contain authentication credentials as URL parameters (e.g., `get.php?username=test&password=test`) and extracts them into separate files for analysis during authorized security assessments.

## Features

- Extract credentials from URLs with `username` and `password` parameters
- Support for both standard URL parameter parsing and regex fallback
- Output credentials to three separate files:
  - `usernames.txt` - List of usernames
  - `passwords.txt` - List of passwords
  - `combo.txt` - Username:password pairs
- Batch processing of multiple URLs from a file
- Custom output directory support
- Quiet mode for minimal output
- Progress tracking with detailed or summary output
- Error handling and validation

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/random-robbie/extract-m3u.git
cd extract-m3u
```

2. Make the script executable:
```bash
chmod +x extract-m3u.py
```

## Usage

### Basic Usage

```bash
python3 extract-m3u.py -f urls.txt
```

### Advanced Usage

```bash
# Specify custom output directory
python3 extract-m3u.py -f urls.txt -o /path/to/output

# Quiet mode (only show summary)
python3 extract-m3u.py -f urls.txt --quiet

# Show help
python3 extract-m3u.py --help

# Show version
python3 extract-m3u.py --version
```

### Command-Line Options

- `-f, --file` : **Required**. Path to file containing URLs (one per line)
- `-o, --output` : Output directory for extracted credentials (default: current directory)
- `-q, --quiet` : Quiet mode - only show summary
- `--version` : Show version information
- `-h, --help` : Show help message

## Input Format

Create a text file with one URL per line. Example (`urls.txt`):

```
http://example.com/get.php?username=user1&password=pass1&type=m3u
http://example.com/player_api.php?username=user2&password=pass2
http://example.com/get.php?username=user3&password=pass3&output=ts
```

## Output

The tool generates three files in the specified output directory:

1. **usernames.txt** - One username per line
2. **passwords.txt** - One password per line
3. **combo.txt** - Credential pairs in `username:password` format

### Example Output

```
============================================================
IPTV M3U Credential Extractor
============================================================

[1] Processing: http://example.com/get.php?username=user1&password=pass1
  ✓ Extracted: user1:pass1
[2] Processing: http://example.com/get.php?username=user2&password=pass2
  ✓ Extracted: user2:pass2

============================================================
Summary: 2/2 credentials extracted
Output files saved to: /home/user/output
============================================================
```

## Use Cases

- Security auditing of IPTV services during authorized penetration tests
- Analyzing credential exposure in URLs
- Educational purposes and security research
- Credential management for authorized testing environments

## Security & Legal Notice

**IMPORTANT**: This tool is intended for:
- Authorized security testing and penetration testing only
- Educational purposes and security research
- Analysis of your own systems or systems you have explicit permission to test

**Unauthorized access to computer systems is illegal.** Always ensure you have proper authorization before testing any systems. The authors assume no liability for misuse of this tool.

## Code Improvements (v2.0)

The updated version includes:
- Python 3 compatibility with type hints
- Proper URL parameter parsing using `urllib.parse`
- Modern Python best practices (f-strings, context managers)
- Better error handling and validation
- Progress tracking and detailed output
- Custom output directory support
- Quiet mode for scripting
- Comprehensive documentation and help text
- UTF-8 encoding support
- Empty line handling
- Better regex fallback for non-standard formats

## Author

Created by [@RandomRobbie](https://github.com/random-robbie)

## License

See [LICENSE](LICENSE) file for details.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## Changelog

### Version 2.0
- Complete rewrite with modern Python practices
- Added type hints and comprehensive documentation
- Improved URL parsing with `urllib.parse`
- Added custom output directory support
- Added quiet mode and progress tracking
- Better error handling and validation
- UTF-8 encoding support
- Command-line argument improvements

### Version 1.0
- Initial release
- Basic credential extraction from URLs
