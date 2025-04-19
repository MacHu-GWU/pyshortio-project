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
import dataclasses
from datetime import datetime

from requests import Response

from .model import BaseModel
from .arg import REQ, NA, rm_na
from .type_hint import T_KWARGS
from .paginator import _paginate

if T.TYPE_CHECKING:  # pragma: no cover
    from .client import Client


@dataclasses.dataclass
class Link(BaseModel):
    """
    Link model representing a Short.io shortened link.

    This class provides a Pythonic interface to Short.io link data while maintaining
    access to the raw API response. All link properties are accessed through
    getter methods that retrieve values from the underlying `_data` dictionary,
    providing resilience against API schema changes.

    .. note::

        All properties return None if the corresponding data is not present
        in the raw API response, providing safe access to optional fields.

    Ref:

    - https://developers.short.io/reference/get_api-links
    """

    _data: dict[str, T.Any] = dataclasses.field(default=REQ)

    @property
    def original_url(self) -> T.Optional[str]:
        return self._data.get("originalURL")

    @property
    def cloaking(self) -> T.Optional[bool]:
        return self._data.get("cloaking")

    @property
    def password(self) -> T.Optional[str]:
        return self._data.get("password")

    @property
    def expires_at(self) -> T.Optional[int]:
        return self._data.get("expiresAt")

    @property
    def expired_url(self) -> T.Optional[str]:
        return self._data.get("expiredURL")

    @property
    def title(self) -> T.Optional[str]:
        return self._data.get("title")

    @property
    def tags(self) -> T.Optional[list[str]]:
        return self._data.get("tags")

    @property
    def utm_source(self) -> T.Optional[str]:
        return self._data.get("utmSource")

    @property
    def utm_medium(self) -> T.Optional[str]:
        return self._data.get("utmMedium")

    @property
    def utm_campaign(self) -> T.Optional[str]:
        return self._data.get("utmCampaign")

    @property
    def utm_term(self) -> T.Optional[str]:
        return self._data.get("utmTerm")

    @property
    def utm_content(self) -> T.Optional[str]:
        return self._data.get("utmContent")

    @property
    def ttl(self) -> T.Optional[str]:
        return self._data.get("ttl")

    @property
    def path(self) -> T.Optional[str]:
        return self._data.get("path")

    @property
    def android_url(self) -> T.Optional[str]:
        return self._data.get("androidURL")

    @property
    def iphone_url(self) -> T.Optional[str]:
        return self._data.get("iphoneURL")

    @property
    def created_at(self) -> T.Optional[datetime]:
        created_at_val = self._data.get("createdAt")
        if created_at_val:
            try:
                # Check if it's a string format that needs conversion
                if isinstance(created_at_val, str):
                    return datetime.fromisoformat(created_at_val.replace("Z", "+00:00"))
                # If it's a timestamp
                elif isinstance(created_at_val, (int, float)):
                    return datetime.fromtimestamp(created_at_val)
            except (ValueError, TypeError):  # pragma: no cover
                pass
        return None

    @property
    def clicks_limit(self) -> T.Optional[int]:
        return self._data.get("clicksLimit")

    @property
    def password_contact(self) -> T.Optional[bool]:
        return self._data.get("passwordContact")

    @property
    def skip_qs(self) -> T.Optional[bool]:
        return self._data.get("skipQS")

    @property
    def archived(self) -> T.Optional[bool]:
        return self._data.get("archived")

    @property
    def split_url(self) -> T.Optional[str]:
        return self._data.get("splitURL")

    @property
    def split_percent(self) -> T.Optional[int]:
        return self._data.get("splitPercent")

    @property
    def integration_adroll(self) -> T.Optional[str]:
        return self._data.get("integrationAdroll")

    @property
    def integration_fb(self) -> T.Optional[str]:
        return self._data.get("integrationFB")

    @property
    def integration_ga(self) -> T.Optional[str]:
        return self._data.get("integrationGA")

    @property
    def integration_gtm(self) -> T.Optional[str]:
        return self._data.get("integrationGTM")

    @property
    def id_string(self) -> T.Optional[str]:
        return self._data.get("idString")

    @property
    def id(self) -> T.Optional[str]:
        return self._data.get("id")

    @property
    def short_url(self) -> T.Optional[str]:
        return self._data.get("shortURL")

    @property
    def secure_short_url(self) -> T.Optional[str]:
        return self._data.get("secureShortURL")

    @property
    def redirect_type(self) -> T.Optional[str]:
        return self._data.get("redirectType")

    @property
    def folder_id(self) -> T.Optional[str]:
        return self._data.get("FolderId")

    @property
    def domain_id(self) -> T.Optional[int]:
        return self._data.get("DomainId")

    @property
    def owner_id(self) -> T.Optional[int]:
        return self._data.get("OwnerId")

    @property
    def has_password(self) -> T.Optional[bool]:
        return self._data.get("hasPassword")

    @property
    def user(self) -> T.Optional[dict]:
        return self._data.get("User")

    @property
    def user_id(self) -> T.Optional[int]:
        user = self.user
        if user:
            return user.get("id")
        return None

    @property
    def user_name(self) -> T.Optional[str]:
        user = self.user
        if user:
            return user.get("name")
        return None

    @property
    def user_email(self) -> T.Optional[str]:
        user = self.user
        if user:
            return user.get("email")
        return None

    @property
    def user_photo_url(self) -> T.Optional[str]:
        user = self.user
        if user:
            return user.get("photoURL")
        return None

    @property
    def core_data(self) -> T_KWARGS:
        """
        Get the essential link data in a simplified dictionary.
        """
        return {
            "id": self.id,
            "id_string": self.id_string,
            "original_url": self.original_url,
            "short_url": self.short_url,
            "created_at": self.created_at,
        }


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
        raise_for_status: bool = True,
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
        link_list = [Link(_data=dct) for dct in response.json().get("links", [])]
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
        raise_for_status: bool = True,
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
        raise_for_status: bool = True,
    ):
        """
        Get OpenGraph properties for a specific link.

        Ref:

        - https://developers.short.io/reference/get_links-opengraph-domainid-linkid
        """
        url = f"https://api.short.io/links/opengraph/{domain_id}/{link_id}"
        response = self.http_get(url=url)
        if raise_for_status:
            response.raise_for_status()
        print(response.text)
        return response
