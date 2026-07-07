"""
get_title_id.py
---------------

Scans a bin file for the title ID embedded in the disc.
Modify the `title_re` pattern to improve matching.
"""

import re
import argparse

title_re = re.compile(
    r"((SCUS|SLES|SLUS|SCES|SCPS|SCKA|SCED|SCEL|SCAS|SCAA|SCAJ|SLPS|SLPM)_\d{3}\.\d{2}|(SCUS|SLES|SLUS|SCES|SCPS|SCKA|SCED|SCEL|SCAS|SCAA|SCAJ|SLPS|SLPM)-\d{5})"
)


def get_psx_id(file_path: str):
    try:
        with open(file_path, "rb") as fin:
            fin.seek(32768)  # Skip the first 32768 bytes
            while True:
                buffer = fin.read(4096)
                if not buffer:
                    break  # End of file reached
                buffered = buffer.decode(
                    "ISO-8859-1"
                )  # Assuming ISO-8859-1 encoding for byte to string conversion
                matches = title_re.search(buffered)
                if matches:
                    return matches.group(0)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"IO error: {e}")
    return None


def main():
    parser = argparse.ArgumentParser(description="Extract PSX ID from a file.")
    _ = parser.add_argument(
        "file_path",
        type=str,
        help="Path to the file from which to extract the PSX ID.",
    )
    args = parser.parse_args()
    psx_id = get_psx_id(args.file_path)
    if psx_id:
        print(f"PSX ID: {psx_id}")
    else:
        print("PSX ID not found.")


if __name__ == "__main__":
    main()
