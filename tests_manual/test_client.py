# -*- coding: utf-8 -*-

from rich import print as rprint
from pyshortio.tests.client import client

# for domain in client.list_domains():
#     print(domain.core_data)

hostname = "escsanhe.short.gy"
domain_id = 1341006
link_id = "lnk_5CR8_rFj22NBAWplmg5Qfepjgg"
folder_id = "SSXdvY_dVm6XdClsh7yNV"


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


def test_get_link_info_by_link_id():
    _, link = client.get_link_info_by_link_id(
        link_id=link_id,
    )
    rprint(link.core_data)
    # rprint(link._data)


def test_get_link_info_by_path():
    _, link = client.get_link_info_by_path(
        hostname=hostname,
        path="ab-test",
    )
    rprint(link.core_data)


def test_list_links_by_original_url():
    _, link_list = client.list_links_by_original_url(
        hostname=hostname,
        original_url="https://example.com",
    )
    for link in link_list:
        rprint(link.core_data)


def test_list_folders():
    _, folder_list = client.list_folders(
        domain_id=domain_id,
    )
    for folder in folder_list:
        rprint(folder.core_data)


def test_get_folder():
    _, folder = client.get_folder(
        domain_id=domain_id,
        folder_id=folder_id,
    )
    rprint(folder.core_data)


if __name__ == "__main__":
    """ """
    # test_list_domains()
    # test_get_domain_by_hostname()
    # test_list_links()
    # test_pagi_list_links()
    # test_get_link_opengraph_properties()
    # test_get_link_info_by_link_id()
    # test_get_link_info_by_path()
    # test_list_links_by_original_url()
    # test_list_folders()
    # test_get_folder()
