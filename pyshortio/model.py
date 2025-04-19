# -*- coding: utf-8 -*-

"""
Base model implementation for Short.io API objects.

This module provides the foundational BaseModel class that all Short.io API
object models (such as Domain, Link) inherit from. It handles common functionality
including:

1. Parameter validation for required fields
2. Distinguishing between required and optional parameters
3. Post-initialization validation
4. Common interface methods that all models must implement

The BaseModel class works in conjunction with the sentinel values (REQ, NA)
from the arg module to manage required vs optional fields in a dataclass-friendly way.
This approach allows Short.io API objects to:

- Validate their structure against API requirements
- Convert between API responses and Python objects
- Maintain consistent interfaces across different object types
- Handle missing or optional fields appropriately
"""

import typing as T
import dataclasses

from .exc import ParamError
from .arg import REQ, _REQUIRED, rm_na, T_KWARGS

T_RESPONSE = T.Dict[str, T.Any]


@dataclasses.dataclass
class BaseModel:
    """
    Base class for all Short.io API object models.

    This class provides common functionality for model validation, parameter handling,
    and interface consistency. All Short.io API object models (Domain, Link, etc.)
    should inherit from this class.

    The BaseModel handles validation of required fields and provides methods to
    distinguish between required and optional parameters. It also defines the
    core_data property interface that all models must implement.
    """

    def _validate(self):
        for field in dataclasses.fields(self.__class__):
            if field.init:
                k = field.name
                if getattr(self, k) is REQ:  # pragma: no cover
                    raise ParamError(f"Field {k!r} is required for {self.__class__}.")

    def __post_init__(self):
        self._validate()

    @classmethod
    def _split_req_opt(cls, kwargs: T_KWARGS) -> T.Tuple[T_KWARGS, T_KWARGS]:
        """
        Splits parameters into required and optional dictionaries.

        This is useful when constructing objects or API requests to ensure
        all required parameters are present before sending a request.
        """
        req_kwargs, opt_kwargs = dict(), dict()
        for field in dataclasses.fields(cls):
            if isinstance(field.default, _REQUIRED):
                try:
                    req_kwargs[field.name] = kwargs[field.name]
                except KeyError:
                    raise ParamError(
                        f"{field.name!r} is a required parameter for {cls}!"
                    )
            else:
                try:
                    opt_kwargs[field.name] = kwargs[field.name]
                except KeyError:
                    pass
        opt_kwargs = rm_na(**opt_kwargs)
        return req_kwargs, opt_kwargs

    @property
    def core_data(self) -> T_KWARGS:
        """
        Returns a dictionary containing the essential data of the model.

        This property must be implemented by all subclasses to provide
        a consistent minimal representation of the model's core data.
        """
        raise NotImplementedError
