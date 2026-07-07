"""
api.py
------

Search for game information using its title ID.
"""

import requests
import re
from tools.utils import cache_request

sanitize_re = re.compile(r"([\.\_\- ])")
api_root = "https://api.serialstation.com/v1"


@cache_request
def get_title_id(title_id: str):
    title_id = sanitize_re.sub("", title_id)
    resp = requests.get(f"{api_root}/title-ids/{title_id}", timeout=5)
    resp.raise_for_status()
    return resp.json()
