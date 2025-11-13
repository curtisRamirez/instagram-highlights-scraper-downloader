import json
import logging
from pathlib import Path
from typing import Iterable

LOGGER = logging.getLogger("instagram_highlights_exporters")

def export_highlights_to_json(items: Iterable[dict], output_path: Path) -> None:
    """
    Export the given iterable of highlight items (dicts) to a JSON file.

    The file will contain a list of objects. Parent directories are created if needed.
    """
    output_path = output_path.expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    data = list(items)

    try:
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as exc:
        LOGGER.error("Failed to write JSON to %s: %s", output_path, exc)
        raise