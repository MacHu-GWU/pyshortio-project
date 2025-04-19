# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from datetime import datetime

from requests import Response

from .model import BaseModel
from .arg import REQ, NA, rm_na
from .type_hint import T_KWARGS

if T.TYPE_CHECKING:  # pragma: no cover
    from .client import Client


@dataclasses.dataclass
class Domain(BaseModel):
    """
    Domain model.

    Ref:

    - https://developers.short.io/reference/get_api-domains
    - https://developers.short.io/reference/get_domains-domainid
    - https://developers.short.io/reference/post_domains
    """

    _data: dict[str, T.Any] = dataclasses.field(default=REQ)

    @property
    def id(self) -> T.Optional[int]:
        return self._data.get("id")

    @property
    def hostname(self) -> T.Optional[str]:
        return self._data.get("hostname")

    @property
    def unicode_hostname(self) -> T.Optional[str]:
        return self._data.get("unicodeHostname")

    @property
    def state(self) -> T.Optional[str]:
        return self._data.get("state")

    @property
    def created_at(self) -> T.Optional[datetime]:
        created_at_str = self._data.get("createdAt")
        if created_at_str:
            try:
                return datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))
            except (ValueError, TypeError):  # pragma: no cover
                pass
        else:  # pragma: no cover
            return None

    @property
    def updated_at(self) -> T.Optional[datetime]:
        updated_at_str = self._data.get("updatedAt")
        if updated_at_str:
            try:
                return datetime.fromisoformat(updated_at_str.replace("Z", "+00:00"))
            except (ValueError, TypeError):  # pragma: no cover
                pass
        else:  # pragma: no cover
            return None

    @property
    def team_id(self) -> T.Optional[int]:
        return self._data.get("TeamId")

    @property
    def has_favicon(self) -> T.Optional[bool]:
        return self._data.get("hasFavicon")

    @property
    def segment_key(self) -> T.Optional[str]:
        return self._data.get("segmentKey")

    @property
    def hide_referer(self) -> T.Optional[bool]:
        return self._data.get("hideReferer")

    @property
    def link_type(self) -> T.Optional[str]:
        return self._data.get("linkType")

    @property
    def cloaking(self) -> T.Optional[bool]:
        return self._data.get("cloaking")

    @property
    def hide_visitor_ip(self) -> T.Optional[bool]:
        return self._data.get("hideVisitorIp")

    @property
    def enable_ai(self) -> T.Optional[bool]:
        return self._data.get("enableAI")

    @property
    def https_level(self) -> T.Optional[str]:
        return self._data.get("httpsLevel")

    @property
    def https_links(self) -> T.Optional[bool]:
        return self._data.get("httpsLinks")

    @property
    def redirect_404(self) -> T.Optional[str]:
        return self._data.get("redirect404")

    @property
    def webhook_url(self) -> T.Optional[str]:
        return self._data.get("webhookURL")

    @property
    def integration_ga(self) -> T.Optional[str]:
        return self._data.get("integrationGA")

    @property
    def integration_fb(self) -> T.Optional[str]:
        return self._data.get("integrationFB")

    @property
    def integration_adroll(self) -> T.Optional[str]:
        return self._data.get("integrationAdroll")

    @property
    def integration_gtm(self) -> T.Optional[str]:
        return self._data.get("integrationGTM")

    @property
    def client_storage(self) -> T.Optional[dict]:
        return self._data.get("clientStorage")

    @property
    def case_sensitive(self) -> T.Optional[bool]:
        return self._data.get("caseSensitive")

    @property
    def increment_counter(self) -> T.Optional[str]:
        return self._data.get("incrementCounter")

    @property
    def robots(self) -> T.Optional[str]:
        return self._data.get("robots")

    @property
    def ssl_cert_expiration_date(self) -> T.Optional[datetime]:
        expiration_date_str = self._data.get("sslCertExpirationDate")
        if expiration_date_str:
            try:
                return datetime.fromisoformat(
                    expiration_date_str.replace("Z", "+00:00")
                )
            except (ValueError, TypeError):  # pragma: no cover
                pass
        else:  # pragma: no cover
            return None

    @property
    def ssl_cert_installed_success(self) -> T.Optional[bool]:
        return self._data.get("sslCertInstalledSuccess")

    @property
    def domain_registration_id(self) -> T.Optional[int]:
        return self._data.get("domainRegistrationId")

    @property
    def user_id(self) -> T.Optional[int]:
        return self._data.get("UserId")

    @property
    def export_enabled(self) -> T.Optional[bool]:
        return self._data.get("exportEnabled")

    @property
    def ip_exclusions(self) -> T.Optional[list[str]]:
        return self._data.get("ipExclusions")

    @property
    def user_plan(self) -> T.Optional[str]:
        return self._data.get("userPlan")

    @property
    def core_data(self) -> T_KWARGS:
        return {
            "id": self.id,
            "hostname": self.hostname,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class DomainMixin:
    def list_domains(
        self: "Client",
        limit: T.Optional[int] = NA,
        offset: T.Optional[int] = NA,
        no_team_id: T.Optional[bool] = NA,
        pattern: T.Optional[str] = NA,
        team_id: T.Optional[str] = NA,
        raise_for_status: bool = True,
    ) -> tuple[Response, list[Domain]]:
        """
        Ref:

        - https://developers.short.io/reference/get_api-domains
        """
        url = f"{self.endpoint}/api/domains"
        params = {
            "limit": limit,
            "offset": offset,
            "noTeamId": no_team_id,
            "pattern": pattern,
            "teamId": team_id,
        }
        params = rm_na(**params)
        response = self.http_get(
            url=url,
            params=params,
        )
        if raise_for_status:
            response.raise_for_status()
        domain_list = [Domain(_data=dct) for dct in response.json()]
        return response, domain_list

    def get_domain(
        self: "Client",
        id: int,
        raise_for_status: bool = True,
    ) -> tuple[Response, T.Optional[Domain]]:
        """
        Ref:

        - https://developers.short.io/reference/get_domains-domainid
        """
        url = f"{self.endpoint}/api/domains/{id}"
        response = self.http_get(
            url=url,
        )
        if raise_for_status:
            response.raise_for_status()
        if response.status_code == 404:
            domain = None
        else:
            domain = Domain(_data=response.json())
        return response, domain

    def get_domain_by_hostname(
        self: "Client",
        hostname: str,
        raise_for_status: bool = True,
    ) -> T.Tuple[Response, T.Optional[Domain]]:
        response, domain_list = self.list_domains(raise_for_status=raise_for_status)
        for domain in domain_list:
            if domain.hostname == hostname:
                return response, domain
        return response, None
