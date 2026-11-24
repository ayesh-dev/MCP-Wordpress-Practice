import requests

SITE_URL = "http://mcp-practice.local"
USERNAME = "ayesha"
APP_PASSWORD = "xxxx xxxx xxxx xxxx xxxx xxxx"


def get_site_info():
    """Return the site name and URL from the WordPress REST API root."""
    response = requests.get(f"{SITE_URL}/wp-json/")
    return response.json()


def list_pages(limit=5):
    """Return the latest published pages as (id, title) pairs."""
    response = requests.get(
        f"{SITE_URL}/wp-json/wp/v2/pages",
        params={"per_page": limit},
        auth=(USERNAME, APP_PASSWORD),
    )
    return [(page["id"], page["title"]["rendered"]) for page in response.json()]
