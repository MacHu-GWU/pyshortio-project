# -*- coding: utf-8 -*-

from pathlib import Path
import polars as pl
from pyshortio.tests.client import client

hostname = "pyshortio.short.gy"
path_tsv = Path("links.tsv")
_, domain = client.get_domain_by_hostname(hostname=hostname)


def reset_shortio():
    link_ids = []
    for _, link_list in client.pagi_list_links(domain_id=domain.id):
        for link in link_list:
            link_ids.append(link.id)

    client.batch_delete_links(link_ids=link_ids)


def sync_tsv():
    with path_tsv.open("r") as file:
        client.sync_tsv(
            hostname=hostname,
            file=file,
            update_if_not_the_same=True,
            delete_if_not_in_file=True,
            # real_run=True,
            real_run=False,
        )


# reset_shortio()
sync_tsv()
