# -*- coding: utf-8 -*-

from datetime import datetime

from .arg import _NOTHING


def datetime_to_iso_string(dt: _NOTHING | datetime) -> _NOTHING | str:
    if isinstance(dt, datetime):
        return dt.isoformat()
    else:
        return dt
