#!/usr/bin/env python3
import csv
import math
from typing import List

"""This file handles pagination"""


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
    DATA_FILE = "pagination/Popular_Baby_Names.csv"

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
            return[]
        
        return dataset[start:end]
