#!/usr/bin/env python3
import csv
import math
import os
from typing import List

"""
Module for implementing simple pagination of a dataset.

This module provides a function to calculate index ranges
and a Server class to paginate a CSV dataset.

Provides:
- index_range function
- Server class for paginating CSV data
"""


def index_range(page, page_size):
    """
    This function uses arguments page number and page_size number:
    It returns the first and last index of the page

    Args:
    page
    page_size

    Return:
    Tuple (first_ind, end_ind)
    """
    #  why (page - 1)? -> computers starts counting from 0
    start_ind = (page - 1) * page_size
    end_ind = page * page_size
    tuple = (start_ind, end_ind)
    return tuple


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = os.path.join(
        os.path.dirname(__file__),
        "Popular_Baby_Names.csv"
     )

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of dataset"""

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()

        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary with hypermedia pagination info."""
        
        data = self.get_page(page, page_size)
        dataset = self.dataset()
        
        total_pages = math.ceil(len(dataset) / page_size) if page_size else 0

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
    