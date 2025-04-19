# -*- coding: utf-8 -*-

from pathlib import Path
from ..client import Client

path_token = Path.home() / ".short.io" / "esc_sanhehu" / "sanhe-dev.txt"
token = path_token.read_text().strip()
client = Client(token=token)