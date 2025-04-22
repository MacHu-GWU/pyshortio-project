# -*- coding: utf-8 -*-

from pathlib import Path
from pyshortio.tests.client import client

hostname = "pyshortio.short.gy"
tsv = client.export_to_tsv(
    hostname=hostname,
)
path_tsv = Path("export.tsv")
path_tsv.write_text(tsv)
