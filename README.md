# MCP WordPress Practice

A small Python helper that reads basic information from a WordPress site
through its REST API. Built while practicing the WordPress MCP setup on a
local LocalWP test site.

## Files

| Path | Purpose |
|---|---|
| `wp_client.py` | Functions that call the WordPress REST API |
| `main.py` | Entry point. Prints the site name and the latest pages |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Keeps local files and secrets out of Git |

## Run it

Credentials come from environment variables, so no password lives in the code.

```
pip install -r requirements.txt
set WP_API_USERNAME=your-username
set WP_API_PASSWORD=your-application-password
python main.py
```

`WP_API_URL` is optional and defaults to `http://mcp-practice.local`.
