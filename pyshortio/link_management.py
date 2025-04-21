# -*- coding: utf-8 -*-

"""
"""

try:
    import typing_extensions as T
except ImportError:  # pragma: no cover
    import typing as T

from datetime import datetime

from requests import Response

from .arg import NA, rm_na
from .constants import DEFAULT_RAISE_FOR_STATUS
from .utils import datetime_to_iso_string
from .model import Link


if T.TYPE_CHECKING:  # pragma: no cover
    from .client import Client


class T_CREATE_BATCH_LINK(T.TypedDict):
    original_url: T.Required[str]
    cloaking: T.NotRequired[bool]
    password: T.NotRequired[str]
    redirect_type: T.NotRequired[str]
    expire_at: T.NotRequired[datetime]
    expire_url: T.NotRequired[str]
    title: T.NotRequired[str]
    tags: T.NotRequired[list[str]]
    utm_source: T.NotRequired[str]
    utm_medium: T.NotRequired[str]
    utm_campaign: T.NotRequired[str]
    utm_term: T.NotRequired[str]
    utm_content: T.NotRequired[str]
    ttl: T.NotRequired[datetime]
    path: T.NotRequired[str]
    android_url: T.NotRequired[str]
    iphone_url: T.NotRequired[str]
    created_at: T.NotRequired[datetime]
    clicks_limit: T.NotRequired[int]
    password_contact: T.NotRequired[bool]
    skip_qs: T.NotRequired[bool]
    archived: T.NotRequired[bool]
    split_url: T.NotRequired[str]
    split_percent: T.NotRequired[int]
    integration_adroll: T.NotRequired[str]
    integration_fb: T.NotRequired[str]
    integration_ga: T.NotRequired[str]
    integration_gtm: T.NotRequired[str]
    allow_duplicates: T.NotRequired[bool]
    folder_id: T.NotRequired[str]


class T_CREATE_LINK(T_CREATE_BATCH_LINK):
    hostname: T.Required[str]


class LinkManagementMixin:
    """ """

    def create_link(
        self: "Client",
        hostname: str,
        original_url: str,
        cloaking: bool = NA,
        password: str = NA,
        redirect_type: str = NA,
        expire_at: datetime = NA,
        expire_url: str = NA,
        title: str = NA,
        tags: list[str] = NA,
        utm_source: str = NA,
        utm_medium: str = NA,
        utm_campaign: str = NA,
        utm_term: str = NA,
        utm_content: str = NA,
        ttl: datetime = NA,
        path: str = NA,
        android_url: str = NA,
        iphone_url: str = NA,
        created_at: datetime = NA,
        clicks_limit: int = NA,
        password_contact: bool = NA,
        skip_qs: bool = NA,
        archived: bool = NA,
        split_url: str = NA,
        split_percent: int = NA,
        integration_adroll: str = NA,
        integration_fb: str = NA,
        integration_ga: str = NA,
        integration_gtm: str = NA,
        allow_duplicates: bool = NA,
        folder_id: str = NA,
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> tuple[Response, T.Optional[Link]]:
        """

        Ref:

        - https://developers.short.io/reference/post_links
        """
        url = f"{self.endpoint}/links"
        data = {
            "domain": hostname,
            "originalURL": original_url,
            "cloaking": cloaking,
            "password": password,
            "redirectType": redirect_type,
            "expiresAt": datetime_to_iso_string(expire_at),
            "expiredURL": expire_url,
            "title": title,
            "tags": tags,
            "utmSource": utm_source,
            "utmMedium": utm_medium,
            "utmCampaign": utm_campaign,
            "utmTerm": utm_term,
            "utmContent": utm_content,
            "ttl": datetime_to_iso_string(ttl),
            "path": path,
            "androidURL": android_url,
            "iphoneURL": iphone_url,
            "createdAt": datetime_to_iso_string(created_at),
            "clicksLimit": clicks_limit,
            "passwordContact": password_contact,
            "skipQS": skip_qs,
            "archived": archived,
            "splitURL": split_url,
            "splitPercent": split_percent,
            "integrationAdroll": integration_adroll,
            "integrationFB": integration_fb,
            "integrationGA": integration_ga,
            "integrationGTM": integration_gtm,
            "allowDuplicates": allow_duplicates,
            "folderId": folder_id,
        }
        data = rm_na(**data)
        response = self.http_post(
            url=url,
            data=data,
        )
        if raise_for_status:
            response.raise_for_status()
        if response.status_code == 200:
            link = Link(_data=response.json())
        else: # pragma: no cover
            raise NotImplementedError("Unexpected response code")
        return response, link

    def batch_create_links(
        self: "Client",
        hostname: str,
        links: list[T_CREATE_BATCH_LINK],
        allow_duplicates: bool = NA,
        folder_id: str = NA,
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> tuple[Response, T.Optional[list[Link]]]:
        """
        Ref:

        - https://developers.short.io/reference/post_links-bulk
        """
        links = [
            rm_na(
                **{
                    "originalURL": dct["original_url"],
                    "cloaking": dct.get("cloaking", NA),
                    "password": dct.get("password", NA),
                    "redirectType": dct.get("redirect_type", NA),
                    "expiresAt": datetime_to_iso_string(dct.get("expires_at", NA)),
                    "expiredURL": dct.get("expired_url", NA),
                    "title": dct.get("title", NA),
                    "tags": dct.get("tags", NA),
                    "utmSource": dct.get("utm_source", NA),
                    "utmMedium": dct.get("utm_medium", NA),
                    "utmCampaign": dct.get("utm_campaign", NA),
                    "utmTerm": dct.get("utm_term", NA),
                    "utmContent": dct.get("utm_content", NA),
                    "ttl": datetime_to_iso_string(dct.get("ttl", NA)),
                    "path": dct.get("path", NA),
                    "androidURL": dct.get("android_url", NA),
                    "iphoneURL": dct.get("iphone_url", NA),
                    "createdAt": datetime_to_iso_string(dct.get("created_at", NA)),
                    "clicksLimit": dct.get("clicks_limit", NA),
                    "passwordContact": dct.get("password_contact", NA),
                    "skipQS": dct.get("skip_qs", NA),
                    "archived": dct.get("archived", NA),
                    "splitURL": dct.get("split_url", NA),
                    "splitPercent": dct.get("split_percent", NA),
                    "integrationAdroll": dct.get("integration_adroll", NA),
                    "integrationFB": dct.get("integration_fb", NA),
                    "integrationGA": dct.get("integration_ga", NA),
                    "integrationGTM": dct.get("integration_gtm", NA),
                    "allowDuplicates": dct.get("allow_duplicates", NA),
                }
            )
            for dct in links
        ]
        data = {
            "domain": hostname,
            "links": links,
            "allowDuplicates": allow_duplicates,
            "folderId": folder_id,
        }
        data = rm_na(**data)
        url = f"{self.endpoint}/links/bulk"
        response = self.http_post(
            url=url,
            data=data,
        )
        if raise_for_status:
            response.raise_for_status()
        if response.status_code == 200:
            link_list = [Link(_data=dct) for dct in response.json()]
        else:  # pragma: no cover
            raise NotImplementedError("Unexpected response code")
        return response, link_list

    def update_link(
        self: "Client",
        link_id: str,
        domain_id: int = NA,
        original_url: str = NA,
        cloaking: bool = NA,
        password: str = NA,
        redirect_type: str = NA,
        expire_at: datetime = NA,
        expire_url: str = NA,
        title: str = NA,
        tags: list[str] = NA,
        utm_source: str = NA,
        utm_medium: str = NA,
        utm_campaign: str = NA,
        utm_term: str = NA,
        utm_content: str = NA,
        ttl: datetime = NA,
        path: str = NA,
        android_url: str = NA,
        iphone_url: str = NA,
        created_at: datetime = NA,
        clicks_limit: int = NA,
        password_contact: bool = NA,
        skip_qs: bool = NA,
        archived: bool = NA,
        split_url: str = NA,
        split_percent: int = NA,
        integration_adroll: str = NA,
        integration_fb: str = NA,
        integration_ga: str = NA,
        integration_gtm: str = NA,
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> tuple[Response, T.Optional[Link]]:
        """

        Ref:

        - https://developers.short.io/reference/post_links-linkid
        """
        url = f"{self.endpoint}/links/{link_id}"
        params = {
            "domain_id": domain_id,
        }
        params = rm_na(**params)
        data = {
            "originalURL": original_url,
            "cloaking": cloaking,
            "password": password,
            "redirectType": redirect_type,
            "expiresAt": datetime_to_iso_string(expire_at),
            "expiredURL": expire_url,
            "title": title,
            "tags": tags,
            "utmSource": utm_source,
            "utmMedium": utm_medium,
            "utmCampaign": utm_campaign,
            "utmTerm": utm_term,
            "utmContent": utm_content,
            "ttl": datetime_to_iso_string(ttl),
            "path": path,
            "androidURL": android_url,
            "iphoneURL": iphone_url,
            "createdAt": datetime_to_iso_string(created_at),
            "clicksLimit": clicks_limit,
            "passwordContact": password_contact,
            "skipQS": skip_qs,
            "archived": archived,
            "splitURL": split_url,
            "splitPercent": split_percent,
            "integrationAdroll": integration_adroll,
            "integrationFB": integration_fb,
            "integrationGA": integration_ga,
            "integrationGTM": integration_gtm,
        }
        data = rm_na(**data)
        response = self.http_post(
            url=url,
            params=params,
            data=data,
        )
        if raise_for_status:
            response.raise_for_status()
        if response.status_code == 200:
            link = Link(_data=response.json())
        elif response.status_code == 400:
            link = None
        elif response.status_code == 404:
            link = None
        else:
            raise NotImplementedError("Unexpected response code")
        return response, link

    def delete_link(
        self: "Client",
        link_id: str,
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> tuple[Response, T.Optional[bool]]:
        """
        Ref:

        - https://developers.short.io/reference/delete_links-link-id
        """
        url = f"{self.endpoint}/links/{link_id}"
        response = self.http_delete(
            url=url,
        )
        if raise_for_status:
            response.raise_for_status()
        if response.status_code == 200:
            success = response.json()["success"]
        elif response.status_code == 404:
            success = False
        else:  # pragma: no cover
            raise NotImplementedError("Unexpected response code")
        return response, success

    def batch_delete_links(
        self: "Client",
        link_ids: list[str],
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> tuple[Response, T.Optional[bool]]:
        """
        Ref:

        - https://developers.short.io/reference/delete_links-delete-bulk
        """
        url = f"{self.endpoint}/links/delete_bulk"
        data = {
            "link_ids": link_ids,
        }
        data = rm_na(**data)
        response = self.http_delete(
            url=url,
            data=data,
        )
        if raise_for_status:
            response.raise_for_status()
        if response.status_code == 200:
            success = response.json()["success"]
        else:
            success = None
        return response, success
