#!/usr/bin/env python3
"""
extract-m3u.py - Extracts usernames and passwords from IPTV M3U URLs.

This tool parses IPTV URLs containing username and password parameters
(e.g., get.php?username=test&password=test) and extracts the credentials
for security testing and analysis purposes.

Author: @RandomRobbie
"""

import sys
import argparse
import os.path
import re
from typing import Optional, Tuple
from urllib.parse import parse_qs, urlparse


def extract_credentials(url: str) -> Optional[Tuple[str, str]]:
    """
    Extract username and password from a URL.

    Args:
        url: URL string potentially containing username and password parameters

    Returns:
        Tuple of (username, password) if found, None otherwise
    """
    try:
        # Try parsing as URL parameters first (more robust)
        parsed = urlparse(url)
        params = parse_qs(parsed.query)

        if 'username' in params and 'password' in params:
            username = params['username'][0]
            password = params['password'][0]
            return (username, password)

        # Fallback to regex for non-standard formats
        username_match = re.search(r'username=([^&\s]+)', url)
        password_match = re.search(r'password=([^&\s]+)', url)

        if username_match and password_match:
            return (username_match.group(1), password_match.group(1))

        return None

    except Exception as e:
        print(f'Error parsing URL: {e}')
        return None


def save_credentials(username: str, password: str, output_dir: str = ".") -> None:
    """
    Save extracted credentials to output files.

    Args:
        username: Extracted username
        password: Extracted password
        output_dir: Directory to save output files (default: current directory)
    """
    try:
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Save to respective files using context managers
        with open(os.path.join(output_dir, "usernames.txt"), "a", encoding="utf-8") as f:
            f.write(f"{username}\n")

        with open(os.path.join(output_dir, "passwords.txt"), "a", encoding="utf-8") as f:
            f.write(f"{password}\n")

        with open(os.path.join(output_dir, "combo.txt"), "a", encoding="utf-8") as f:
            f.write(f"{username}:{password}\n")

    except IOError as e:
        print(f'Error writing to file: {e}')


def process_file(input_file: str, output_dir: str = ".", verbose: bool = True) -> Tuple[int, int]:
    """
    Process a file containing URLs and extract credentials.

    Args:
        input_file: Path to file containing URLs (one per line)
        output_dir: Directory to save output files
        verbose: Print progress messages

    Returns:
        Tuple of (successful_extractions, total_lines)
    """
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found")
        return (0, 0)

    successful = 0
    total = 0

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                url = line.strip()
                total += 1

                if not url:  # Skip empty lines
                    continue

                if verbose:
                    print(f"[{line_num}] Processing: {url[:80]}..." if len(url) > 80 else f"[{line_num}] Processing: {url}")

                credentials = extract_credentials(url)

                if credentials:
                    username, password = credentials
                    save_credentials(username, password, output_dir)
                    successful += 1
                    if verbose:
                        print(f"  ✓ Extracted: {username}:{password}")
                else:
                    if verbose:
                        print(f"  ✗ No credentials found")

    except KeyboardInterrupt:
        print("\n[!] Ctrl-C pressed, stopping...")
        return (successful, total)
    except Exception as e:
        print(f"Error reading file: {e}")
        return (successful, total)

    return (successful, total)


def main():
    """Main function to parse arguments and run the extractor."""
    parser = argparse.ArgumentParser(
        description='Extract usernames and passwords from IPTV M3U URLs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s -f urls.txt
  %(prog)s -f urls.txt -o output_dir
  %(prog)s -f urls.txt --quiet

Note: This tool is intended for authorized security testing only.
        '''
    )

    parser.add_argument(
        "-f", "--file",
        required=True,
        help="File containing URLs (one per line)"
    )

    parser.add_argument(
        "-o", "--output",
        default=".",
        help="Output directory for extracted credentials (default: current directory)"
    )

    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Quiet mode - only show summary"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 2.0"
    )

    args = parser.parse_args()

    print("=" * 60)
    print("IPTV M3U Credential Extractor")
    print("=" * 60)
    print()

    successful, total = process_file(args.file, args.output, verbose=not args.quiet)

    print()
    print("=" * 60)
    print(f"Summary: {successful}/{total} credentials extracted")
    print(f"Output files saved to: {os.path.abspath(args.output)}")
    print("=" * 60)


if __name__ == "__main__":
    main()