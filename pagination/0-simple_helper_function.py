#!/usr/bin/env python3
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
