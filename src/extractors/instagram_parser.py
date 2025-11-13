import json
import logging
import re
from dataclasses import dataclass, asdict
from typing import Any, Optional
from urllib.parse import urlparse

import requests

from src.extractors.utils_time import to_unix_timestamp

@dataclass
class HighlightMediaItem:
    username: str
    id: str
    highlightId: str
    highlightTitle: str
    media: str
    mediaType: str
    mentions: list[str]
    timestamp: int
    thumbnail: str

    def to_dict(self) -> dict:
        return asdict(self)

class InstagramHighlightScraper:
    """
    A lightweight, no-auth scraper for Instagram story highlight metadata using the public web pages.

    This is a best-effort implementation that:
    - fetches the profile's public HTML
    - looks for embedded JSON blobs (e.g., window._sharedData style or similar)
    - walks the JSON to find highlight data

    Because Instagram changes its internal structure often, this parser is defensive:
    if it cannot find highlight data, it simply returns an empty list rather than crashing.
    """

    INSTAGRAM_BASE = "https://www.instagram.com"

    def __init__(
        self,
        user_agent: Optional[str] = None,
        timeout: int = 15,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        self.session = requests.Session()
        self.timeout = timeout
        self.logger = logger or logging.getLogger(__name__)
        self.session.headers.update(
            {
                "User-Agent": user_agent
                or (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0 Safari/537.36"
                ),
                "Accept-Language": "en-US,en;q=0.9",
            }
        )

    # --------- Public API ---------

    def scrape_highlights(self, username_or_url: str) -> list[HighlightMediaItem]:
        """
        Main entrypoint: given a username or profile URL, return a list of HighlightMediaItem.
        """
        username = self._normalize_username(username_or_url)
        if not username:
            raise ValueError(f"Could not normalize username from '{username_or_url}'")

        profile_url = f"{self.INSTAGRAM_BASE}/{username}/"
        self.logger.debug("Fetching profile page: %s", profile_url)

        html = self._fetch(profile_url)
        if not html:
            self.logger.warning("No HTML received for %s", profile_url)
            return []

        shared_data = self._extract_embedded_json(html)
        if not shared_data:
            self.logger.warning("No embedded JSON data detected for %s", profile_url)
            return []

        try:
            user_id, highlight_items = self._parse_highlights_from_shared_data(
                shared_data
            )
        except Exception as exc:
            self.logger.error(
                "Error while parsing highlights from JSON for %s: %s",
                username,
                exc,
                exc_info=self.logger.isEnabledFor(logging.DEBUG),
            )
            return []

        items: list[HighlightMediaItem] = []
        for hi in highlight_items:
            items.extend(self._expand_highlight_collection(username, user_id, hi))

        return items

    # --------- Networking helpers ---------

    def _fetch(self, url: str) -> str | None:
        try:
            resp = self.session.get(url, timeout=self.timeout)
            if resp.status_code != 200:
                self.logger.warning(
                    "Request to %s failed with status %s", url, resp.status_code
                )
                return None
            return resp.text
        except requests.RequestException as exc:
            self.logger.error("HTTP error while requesting %s: %s", url, exc)
            return None

    # --------- Parsing helpers ---------

    @staticmethod
    def _normalize_username(username_or_url: str) -> str:
        """
        Accept a raw username or full URL, and return the canonical username.
        """
        s = username_or_url.strip()
        if not s:
            return ""

        if "instagram.com" not in s:
            # assume it's already a username
            return s.strip("@/ ")

        # Parse URL
        parsed = urlparse(s)
        path = parsed.path.strip("/")
        if not path:
            return ""

        # URL can be like /username or /username/anything
        # The username is the first segment
        username = path.split("/")[0]
        return username.strip("@")

    def _extract_embedded_json(self, html: str) -> Optional[dict]:
        """
        Try multiple strategies to extract a big JSON blob from the profile HTML.
        The older pattern is "window._sharedData = {...};", but this may change.
        """
        # Strategy 1: window._sharedData pattern
        shared_match = re.search(