# -*- coding: utf-8 -*-

from datetime import datetime
from pyshortio.arg import _NOTHING, NA
from pyshortio.utils import datetime_to_iso_string


def test_datetime_to_iso_string():
    assert isinstance(datetime_to_iso_string(dt=datetime.utcnow()), str)
    assert isinstance(datetime_to_iso_string(dt=NA), _NOTHING)


if __name__ == "__main__":
    from pyshortio.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyshortio.utils",
        preview=False,
    )
