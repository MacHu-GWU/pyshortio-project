# -*- coding: utf-8 -*-

from rich import print as rprint
from pyshortio.tests.client import client

# for domain in client.list_domains():
#     print(domain.core_data)

hostname = "escsanhe.short.gy"
domain_id = 1341006
link_id = "lnk_5CR8_rFj22NBAWplmg5Qfepjgg"


def test_list_domains():
    _, domain_list = client.list_domains(pattern=hostname)
    for domain in domain_list:
        rprint(domain.core_data)


def test_get_domain_by_hostname():
    _, domain = client.get_domain_by_hostname(hostname)
    rprint(domain.core_data)


def test_list_links():
    _, link_list = client.list_link(
        domain_id=domain_id,
        limit=2,
    )
    for link in link_list:
        rprint(link.core_data)


def test_pagi_list_links():
    for ith, (_, link_list) in enumerate(
        client.pagi_list_links(domain_id=domain_id, limit=2),
        start=1,
    ):
        print(f"{ith}th api call")
        for link in link_list:
            rprint(link.core_data)


def test_get_link_opengraph_properties():
    client.get_link_opengraph_properties(
        domain_id=domain_id,
        link_id=link_id,
    )
    pass


if __name__ == "__main__":
    """ """
    # test_list_domains()
    # test_get_domain_by_hostname()
    # test_list_links()
    test_pagi_list_links()
    # test_get_link_opengraph_properties()
