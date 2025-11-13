import argparse
import json
import logging
import sys
from pathlib import Path
from datetime import datetime

# Ensure project root is on sys.path so "src" is importable as a namespace package
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.extractors.instagram_parser import InstagramHighlightScraper  # type: ignore
from src.outputs.exporters import export_highlights_to_json  # type: ignore

LOGGER = logging.getLogger("instagram_highlights_runner")

def load_config(config_path: Path) -> dict:
    """
    Load JSON config if it exists; otherwise return sensible defaults.
    """
    default_config = {
        "request_timeout": 15,
        "user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        ),
    }

    if not config_path.exists():
        LOGGER.warning("Config file %s not found. Using defaults.", config_path)
        return default_config

    try:
        with config_path.open("r", encoding="utf-8") as f:
            file_config = json.load(f)
    except Exception as exc:
        LOGGER.error("Failed to parse config file %s: %s", config_path, exc)
        return default_config

    merged = {**default_config, **file_config}
    return merged

def read_inputs(input_file: Path) -> list[str]:
    """
    Read usernames or profile URLs from the input file.
    Lines starting with '#' or empty lines are ignored.
    """
    if not input_file.exists():
        LOGGER.error("Input file %s does not exist.", input_file)
        return []

    lines: list[str] = []
    try:
        with input_file.open("r", encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                lines.append(line)
    except Exception as exc:
        LOGGER.error("Failed to read input file %s: %s", input_file, exc)
        return []

    return lines

def determine_output_path(output_arg: str | None) -> Path:
    """
    Determine where to write the final JSON file.
    If the user provided a path, use it, otherwise generate a timestamped file under data/.
    """
    if output_arg:
        output_path = Path(output_arg).expanduser().resolve()
        if output_path.is_dir():
            timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
            return output_path / f"highlights_{timestamp}.json"
        return output_path

    data_dir = PROJECT_ROOT / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    return data_dir / f"highlights_{timestamp}.json"

def configure_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    )

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scrape Instagram story highlights from public profiles."
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to settings JSON (default: src/config/settings.example.json).",
    )
    parser.add_argument(
        "--input",
        type=str,
        help="Path to input file with usernames or profile URLs (default: data/inputs.sample.txt).",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Path to output JSON file or directory (default: data/highlights_*.json).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging.",
    )

    args = parser.parse_args()
    configure_logging(verbose=args.verbose)

    config_path = (
        Path(args.config).expanduser().resolve()
        if args.config
        else PROJECT_ROOT / "src" / "config" / "settings.example.json"
    )

    config = load_config(config_path)

    input_file = (
        Path(args.input).expanduser().resolve()
        if args.input
        else PROJECT_ROOT / "data" / "inputs.sample.txt"
    )

    usernames_or_urls = read_inputs(input_file)
    if not usernames_or_urls:
        LOGGER.error("No valid usernames/profile URLs found in %s. Exiting.", input_file)
        return 1

    output_path = determine_output_path(args.output)

    scraper = InstagramHighlightScraper(
        user_agent=config.get("user_agent"),
        timeout=config.get("request_timeout", 15),
        logger=logging.getLogger("instagram_highlights_scraper"),
    )

    all_items: list[dict] = []

    for item in usernames_or_urls:
        try:
            LOGGER.info("Processing %s", item)
            highlights = scraper.scrape_highlights(item)
            LOGGER.info("Found %d highlight items for %s", len(highlights), item)
            all_items.extend([h.to_dict() for h in highlights])
        except Exception as exc:
            LOGGER.error("Failed to process %s: %s", item, exc, exc_info=args.verbose)

    if not all_items:
        LOGGER.warning("No highlight items were collected. Nothing to export.")
        return 0

    try:
        export_highlights_to_json(all_items, output_path)
        LOGGER.info("Exported %d items to %s", len(all_items), output_path)
    except Exception as exc:
        LOGGER.error("Failed to export data to %s: %s", output_path, exc)
        return 1

    return 0

if __name__ == "__main__":
    raise SystemExit(main())