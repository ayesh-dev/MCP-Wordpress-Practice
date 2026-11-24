import os

import requests

SITE_URL = os.environ.get("WP_API_URL", "http://mcp-practice.local")
USERNAME = os.environ.get("WP_API_USERNAME")
APP_PASSWORD = os.environ.get("WP_API_PASSWORD")


def _require_credentials():
    if not USERNAME or not APP_PASSWORD:
        raise RuntimeError(
            "Set WP_API_USERNAME and WP_API_PASSWORD before running. "
            "See the README."
        )


def get_site_info():
    """Return the site name and URL from the WordPress REST API root."""
    response = requests.get(f"{SITE_URL}/wp-json/", timeout=10)
    response.raise_for_status()
    return response.json()


def list_pages(limit=5):
    """Return the latest published pages as (id, title) pairs."""
    _require_credentials()
    response = requests.get(
        f"{SITE_URL}/wp-json/wp/v2/pages",
        params={"per_page": limit},
        auth=(USERNAME, APP_PASSWORD),
        timeout=10,
    )
    response.raise_for_status()
    return [(page["id"], page["title"]["rendered"]) for page in response.json()]
