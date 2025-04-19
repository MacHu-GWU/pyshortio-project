# -*- coding: utf-8 -*-

from pyshortio import api


def test():
    _ = api


if __name__ == "__main__":
    from pyshortio.tests import run_cov_test

    run_cov_test(
        __file__,
        "pyshortio.api",
        preview=False,
    )
