# -*- coding: utf-8 -*-

from pyshortio import api


def test():
    _ = api
    _ = api.Client.list_domains
    _ = api.Client.get_domain
    _ = api.Client.get_domain_by_hostname
    _ = api.Client.list_links
    _ = api.Client.pagi_list_links
    _ = api.Client.get_link_opengraph_properties
    _ = api.Client.get_link_info_by_link_id
    _ = api.Client.get_link_info_by_path
    _ = api.Client.list_links_by_original_url
    _ = api.Client.list_folders
    _ = api.Client.get_folder
    _ = api.Client.create_link
    _ = api.Client.batch_create_links
    _ = api.Client.update_link
    _ = api.Client.delete_link
    _ = api.Client.batch_delete_links
    _ = api.Client.sync_tsv
    _ = api.Client.export_to_tsv


if __name__ == "__main__":
    from pyshortio.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyshortio.api",
        preview=False,
    )
