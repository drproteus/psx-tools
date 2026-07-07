"""
title.py
--------

Scans a bin file for the title ID embedded in the disc.
Modify the `title_re` pattern to improve matching.
"""

import re

title_re = re.compile(
    r"((SCUS|SLES|SLUS|SCES|SCPS|SCKA|SCED|SCEL|SCAS|SCAA|SCAJ|SLPS|SLPM)_\d{3}\.\d{2}|(SCUS|SLES|SLUS|SCES|SCPS|SCKA|SCED|SCEL|SCAS|SCAA|SCAJ|SLPS|SLPM)-\d{5})"
)


def get_psx_id(file_path: str) -> str | None:
    try:
        with open(file_path, "rb") as fin:
            _ = fin.seek(32768)  # Skip the first 32768 bytes
            while buffer := fin.read(4096):
                buffered = buffer.decode("ISO-8859-1")
                matches = title_re.search(buffered)
                if matches:
                    return matches.group(0)
    except Exception:
        pass
