# -*- coding: utf-8 -*-

from pathlib import Path
from ..client import Client

path_token = Path.home() / ".short.io" / "sanhehu_esc" / "sanhe-dev.txt"
token = path_token.read_text().strip()
client = Client(token=token)