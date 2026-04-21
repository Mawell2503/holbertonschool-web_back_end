#!/usr/bin/env python3
"""This file handles pagination"""


def index_range(page, page_size):
    #  why (page - 1)? -> computers starts counting from 0
    start_ind = (page - 1) * page_size
    end_ind = page * page_size
    tuple = (start_ind, end_ind)
    return tuple
