from __future__ import annotations

import datetime
from typing import Any

def to_unix_timestamp(value: Any) -> int:
    """
    Convert a variety of timestamp-ish values into a Unix timestamp (seconds).

    Supported formats:
    - int or float: assumed to already be a Unix timestamp
    - str of digits: parsed as int Unix timestamp
    - ISO-like datetime strings: parsed best-effort as UTC
    - datetime.datetime objects

    On failure, this returns 0 so callers don't have to guard against None.
    """
    if value is None:
        return 0

    # datetime instance
    if isinstance(value, datetime.datetime):
        if value.tzinfo is None:
            value = value.replace(tzinfo=datetime.timezone.utc)
        return int(value.timestamp())

    # int or float
    if isinstance(value, (int, float)):
        # Heuristic: if value seems to be in milliseconds, convert to seconds
        if value > 10_000_000_000:  # > ~2286-11-20 in seconds
            return int(value / 1000)
        return int(value)

    # string
    if isinstance(value, str):
        s = value.strip()
        if not s:
            return 0

        # Digit-only: interpret as Unix timestamp
        if s.isdigit():
            try:
                iv = int(s)
            except ValueError:
                return 0
            if iv > 10_000_000_000:
                return int(iv / 1000)
            return iv

        # Try several datetime formats
        formats = [
            "%Y-%m-%dT%H:%M:%S.%fZ",
            "%Y-%m-%dT%H:%M:%SZ",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d",
        ]
        for fmt in formats:
            try:
                dt = datetime.datetime.strptime(s, fmt)
                dt = dt.replace(tzinfo=datetime.timezone.utc)
                return int(dt.timestamp())
            except ValueError:
                continue

    # Fallback: unknown format
    return 0