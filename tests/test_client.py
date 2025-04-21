# -*- coding: utf-8 -*-

import os
import pytest
from pyshortio.client import normalize_endpoint
from pyshortio.tests.client import IS_CI, client


def test_normalize_endpoint():
    assert normalize_endpoint("https://api.short.io/") == "https://api.short.io"


@pytest.mark.skipif(IS_CI, reason="Skip on CI")
class TestClient:
    hostname: str = "pyshortio.short.gy"
    domain_id: int = None

    @classmethod
    def setup_class(cls):
        _, domain = client.get_domain_by_hostname(
            hostname=cls.hostname,
        )
        cls.domain_id = domain.id

        link_ids = list()
        for _, link_list in client.pagi_list_links(
            domain_id=cls.domain_id,
            limit=100,
        ):
            for link in link_list:
                link_ids.append(link.id)

        if len(link_ids):
            client.batch_delete_links(link_ids=link_ids)

    def _test_01_get_domain(self):
        _, domain = client.get_domain(domain_id=self.domain_id)
        assert domain.id == self.domain_id
        assert domain.hostname == self.hostname

    def _test_02_create_link(self):
        _, link = client.create_link(
            hostname=self.hostname,
            title="Short io pricing",
            original_url="https://short.io/pricing/",
        )
        self.link_pricing = link
        assert self.link_pricing.title == "Short io pricing"
        assert self.link_pricing.original_url == "https://short.io/pricing/"

        _, links = client.batch_create_links(
            hostname=self.hostname,
            links=[
                {
                    "title": "Short io features",
                    "original_url": "https://short.io/features/",
                },
                {
                    "title": "Short io integrations",
                    "original_url": "https://short.io/integrations/",
                },
            ],
        )
        self.link_features = links[0]
        self.link_integrations = links[1]

        assert self.link_features.title == "Short io features"
        assert self.link_features.original_url == "https://short.io/features/"
        assert self.link_integrations.title == "Short io integrations"
        assert self.link_integrations.original_url == "https://short.io/integrations/"

    def _test_03_list_and_get_links(self):
        _, link_list = client.list_links(
            domain_id=self.domain_id,
            limit=2,
        )
        assert len(link_list) == 2

        _, link_list = client.list_links(
            domain_id=self.domain_id,
        )
        assert len(link_list) == 3

        _, link_list = client.list_links(
            domain_id=self.domain_id,
            limit=100,
        )
        assert len(link_list) == 3

        paginator = client.pagi_list_links(
            domain_id=self.domain_id,
            limit=2,
        )
        results = list(paginator)
        assert len(results) == 2

        assert len(results[0][1]) == 2
        assert len(results[1][1]) == 1

        _, result = client.get_link_opengraph_properties(
            domain_id=self.domain_id,
            link_id=self.link_pricing.id,
        )

        _, link = client.get_link_info_by_link_id(link_id=self.link_pricing.id)
        assert link.id == self.link_pricing.id

        _, link = client.get_link_info_by_link_id(
            link_id="not-exists",
            raise_for_status=False,
        )
        assert link is None

        _, link = client.get_link_info_by_path(
            hostname=self.hostname,
            path=self.link_pricing.path,
        )
        assert link.id == self.link_pricing.id
        assert link.path == self.link_pricing.path

        _, link = client.get_link_info_by_path(
            hostname=self.hostname,
            path="not-exists",
            raise_for_status=False,
        )
        assert link is None

        _, link_list = client.list_links_by_original_url(
            hostname=self.hostname,
            original_url=self.link_pricing.original_url,
        )
        assert len(link_list) == 1
        link = link_list[0]
        assert link.id == self.link_pricing.id
        assert link.original_url == self.link_pricing.original_url

        _, link_list = client.list_links_by_original_url(
            hostname=self.hostname,
            original_url="not-exists",
            raise_for_status=False,
        )
        assert len(link_list) == 0

        _, folder_list = client.list_folders(domain_id=self.domain_id)
        assert len(folder_list) == 0

        _, folder = client.get_folder(
            domain_id=self.domain_id,
            folder_id="not-exists",
            raise_for_status=False,
        )
        assert folder is None

    def _test_04_update_and_delete(self):
        _, link = client.update_link(
            link_id=self.link_pricing.id,
            title="Short io pricing updated",
            original_url="https://short.io/pricing/updated",
        )
        assert link.id == self.link_pricing.id
        assert link.title == "Short io pricing updated"
        assert link.original_url == "https://short.io/pricing/updated"

        _, link = client.get_link_info_by_link_id(link_id=self.link_pricing.id)
        assert link.id == self.link_pricing.id
        assert link.title == "Short io pricing updated"
        assert link.original_url == "https://short.io/pricing/updated"

        _, link = client.update_link(
            link_id="not-exists",
            raise_for_status=False,
        )
        assert link is None

        _, link = client.update_link(
            link_id="lnk_1a2b_3333cccc4444dddd55555",
            raise_for_status=False,
        )
        assert link is None

        _, success = client.delete_link(
            link_id=self.link_pricing.id,
        )
        assert success is True

        _, success = client.delete_link(
            link_id="not-exists",
            raise_for_status=False,
        )
        assert success is False

        _, link_list = client.list_links(
            domain_id=self.domain_id,
            limit=100,
        )
        assert len(link_list) == 2

    def test(self):
        self._test_01_get_domain()
        self._test_02_create_link()
        self._test_03_list_and_get_links()
        self._test_04_update_and_delete()


if __name__ == "__main__":
    from pyshortio.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyshortio",
        preview=False,
    )
