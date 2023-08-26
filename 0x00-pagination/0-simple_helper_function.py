#!/usr/bin/env python3

"""
Module containing the simple helper function index_range
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates index dependin gon page parameters

    Args:
    page (int) - the number of the page
    page_size (int) - the size of data in a page

    Return:
    value (tuple) - tuple of size two bearing start and end index
    """
    return (page_size * (page - 1), page_size)
