# -*- coding: utf-8 -*-

"""
Short.io Link query API implementation.

This module provides classes and methods for interacting with the Short.io Link-related
API endpoints. It includes both the data model for Link objects and the API query
methods for retrieving and manipulating links.

The implementation follows three key design patterns:

1. **Raw Data Storage Pattern**:

All Short.io data class objects (like Link) have an attribute called `_data` that
stores the raw data from HTTP responses. This approach treats the Short.io API
response as having an unstable schema, storing raw values as-is and using lazy-loaded
properties to access the data instead of defining them as attributes. This provides
resilience against API changes and ensures backward compatibility.

Example:

    >>> link = Link(_data=data_from_response)
    >>> link.original_url  # Access through property, not direct attribute

2. **Return Pattern**:

All methods representing Short.io API calls return a tuple of two objects:

- First: The raw `requests.Response` object, allowing users complete access to
  HTTP response details (headers, status codes, etc.)
- Second: A method-specific result in a Pythonic format (e.g., a list of Link objects)

Each method includes a `raise_for_status` parameter that controls whether
exceptions are raised immediately on HTTP errors, giving users fine-grained control
over error handling.

3. **Pagination Abstraction Pattern**:

Short.io API list methods use next page tokens for pagination. This module implements
a universal pagination mechanism that converts any regular API method to an
auto-paginating method. These methods are prefixed with `pagi_` followed by the
original method name and return an iterable of the original method's return values
(typically tuples of response and specialized objects).

This approach provides a balance between raw API access and Pythonic convenience,
giving users flexibility in how they interact with the Short.io API.
"""

import typing as T
from datetime import datetime

from requests import Response

from .arg import NA, rm_na
from .constants import DEFAULT_RAISE_FOR_STATUS
from .model import Link, Folder
from .paginator import _paginate


if T.TYPE_CHECKING:  # pragma: no cover
    from .client import Client


class LinkQueriesMixin:
    """
    Mixin class providing Link-related API methods for the Client.

    This class implements various methods for interacting with Short.io Link
    API endpoints. When combined with the main Client class, it provides
    a comprehensive interface for managing links.

    All methods follow the Dual Return Pattern, returning both the raw HTTP
    response and a Pythonic representation of the API result.

    Methods prefixed with `pagi_` implement the Pagination Abstraction Pattern,
    automatically handling pagination for list operations.
    """

    def list_link(
        self: "Client",
        domain_id: int,
        limit: T.Optional[int] = NA,
        id_string: T.Optional[int] = NA,
        create_at: T.Optional[datetime] = NA,
        before_date: T.Optional[datetime] = NA,
        after_date: T.Optional[datetime] = NA,
        date_sort_order: T.Optional[str] = NA,
        page_token: T.Optional[str] = NA,
        folder_id: T.Optional[str] = NA,
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> tuple[Response, list[Link]]:
        """
        List links for a specific domain with optional filtering.

        This method retrieves links from the Short.io API with various filtering options.
        It follows the Dual Return Pattern, providing both raw HTTP access and
        Pythonic data models.

        Ref:

        - https://developers.short.io/reference/get_api-domains
        """
        url = f"{self.endpoint}/api/links"
        params = {
            "domain_id": domain_id,
            "limit": limit,
            "idString": id_string,
            "createdAt": create_at,
            "beforeDate": before_date,
            "afterDate": after_date,
            "dateSortOrder": date_sort_order,
            "pageToken": page_token,
            "folderId": folder_id,
        }
        params = rm_na(**params)
        response = self.http_get(
            url=url,
            params=params,
        )
        if raise_for_status:
            response.raise_for_status()
        if response.status_code == 200:
            link_list = [Link(_data=dct) for dct in response.json().get("links", [])]
        else:
            raise NotImplementedError("Unexpected response code")
        return response, link_list

    def pagi_list_links(
        self: "Client",
        domain_id: int,
        limit: T.Optional[int] = NA,
        id_string: T.Optional[int] = NA,
        create_at: T.Optional[datetime] = NA,
        before_date: T.Optional[datetime] = NA,
        after_date: T.Optional[datetime] = NA,
        date_sort_order: T.Optional[str] = NA,
        folder_id: T.Optional[str] = NA,
        total_max_results: int = 9999,
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> T.Iterable[tuple[Response, list[Link]]]:
        """
        Auto-paginated version of list_link method.

        This method implements the Pagination Abstraction Pattern, automatically
        handling pagination for listing links. It returns an iterable that yields
        each page of results, allowing for efficient processing of large result sets.

        >>> # Process all links across multiple pages
        >>> for response, links in client.pagi_list_links(domain_id=123):
        >>>     for link in links:
        >>>         process_link(link)

        .. note::

            This method automatically handles fetching subsequent pages until
        """

        def get_next_token(res):
            return res.get("nextPageToken")

        def set_next_token(kwargs, next_token):
            kwargs["page_token"] = next_token

        yield from _paginate(
            method=self.list_link,
            list_key="links",
            get_next_token=get_next_token,
            set_next_token=set_next_token,
            kwargs=dict(
                domain_id=domain_id,
                limit=limit,
                id_string=id_string,
                create_at=create_at,
                before_date=before_date,
                after_date=after_date,
                date_sort_order=date_sort_order,
                folder_id=folder_id,
                raise_for_status=raise_for_status,
            ),
            max_results=total_max_results,
        )

    def get_link_opengraph_properties(
        self: "Client",
        domain_id: int,
        link_id: str,
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> tuple[Response, T.Optional[list]]:
        """
        Get OpenGraph properties for a specific link.

        Ref:

        - https://developers.short.io/reference/get_links-opengraph-domainid-linkid
        """
        url = f"https://api.short.io/links/opengraph/{domain_id}/{link_id}"
        response = self.http_get(url=url)
        if raise_for_status:
            response.raise_for_status()
        if response.status_code == 200:
            result = response.json()
        else:  # pragma: no cover
            raise NotImplementedError("Unexpected response code")
        return response, result

    def get_link_info_by_link_id(
        self: "Client",
        link_id: str,
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> tuple[Response, Link]:
        """
        Get link information by link ID.

        Ref:

        - https://developers.short.io/reference/get_links-linkid
        """
        url = f"{self.endpoint}/links/{link_id}"
        response = self.http_get(url=url)
        if raise_for_status:
            response.raise_for_status()
        if response.status_code == 200:
            link = Link(_data=response.json())
        elif response.status_code == 404:
            link = None
        else:  # pragma: no cover
            raise NotImplementedError("Unexpected response code")
        return response, link

    def get_link_info_by_path(
        self: "Client",
        hostname: str,
        path: str,
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> tuple[Response, Link]:
        """
        Get link information by link ID.

        Ref:

        - https://developers.short.io/reference/get_links-expand
        """
        url = f"{self.endpoint}/links/expand"
        params = {
            "domain": hostname,
            "path": path,
        }
        response = self.http_get(url=url, params=params)
        if raise_for_status:
            response.raise_for_status()
        if response.status_code == 200:
            link = Link(_data=response.json())
        elif response.status_code == 404:
            link = None
        else:  # pragma: no cover
            raise NotImplementedError("Unexpected response code")
        return response, link

    def list_links_by_original_url(
        self: "Client",
        hostname: str,
        original_url: str,
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> tuple[Response, list[Link]]:
        """
        Returns all links with the same original URL.

        Ref:

        - https://developers.short.io/reference/get_links-multiple-by-url
        """
        url = f"{self.endpoint}/links/multiple-by-url"
        params = {
            "domain": hostname,
            "originalURL": original_url,
        }
        response = self.http_get(url=url, params=params)
        if raise_for_status:
            response.raise_for_status()
        if response.status_code == 200:
            link_list = [Link(_data=dct) for dct in response.json().get("links", [])]
        elif response.status_code == 404:
            link_list = []
        else:  # pragma: no cover
            raise NotImplementedError("Unexpected response code")
        return response, link_list

    def list_folders(
        self: "Client",
        domain_id: int,
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> tuple[Response, list[Folder]]:
        """
        Ref:

        - https://developers.short.io/reference/get_links-folders-domainid
        """
        url = f"{self.endpoint}/links/folders/{domain_id}"
        response = self.http_get(url=url)
        if raise_for_status:
            response.raise_for_status()
        if response.status_code == 200:
            folder_list = [
                Folder(_data=dct) for dct in response.json().get("linkFolders", [])
            ]
        else:
            raise NotImplementedError("Unexpected response code")
        return response, folder_list

    def get_folder(
        self: "Client",
        domain_id: int,
        folder_id: str,
        raise_for_status: bool = DEFAULT_RAISE_FOR_STATUS,
    ) -> tuple[Response, T.Optional[Folder]]:
        """
        Ref:

        - https://developers.short.io/reference/get_links-folders-domainid-folderid
        """
        url = f"{self.endpoint}/links/folders/{domain_id}/{folder_id}"
        response = self.http_get(url=url)
        if raise_for_status:  # pragma: no cover
            response.raise_for_status()
        if response.status_code == 200:
            response_json = response.json()
            if response_json is None:
                folder = None
            else:
                folder = Folder(_data=response.json())
        elif response.status_code == 404:  # pragma: no cover
            folder = None
        else:  # pragma: no cover
            raise NotImplementedError("Unexpected response code")
        return response, folder
