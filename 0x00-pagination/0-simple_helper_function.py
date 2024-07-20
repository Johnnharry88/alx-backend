#!/usr/bin/env python3
""" A fucntion that takes two arguents of integer and  returns a tuple """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Start and end index that matches with range"""
    return ((page - 1) * page_size, page_size * page)
