#!/usr/bin/env python3
""" A fucntion that takes two arguents of integer and  returns a tuple """


from typing import Tuple, List
import math
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Start and end index that matches with range"""
    return ((page - 1) * page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of dataset from database"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        # get data from the file
        database = self.dataset()

        try:
            # fix the begining and ending of pagination
            begin, stop = index_range(page, page_size)
            return database[begin:stop]

        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns dictonary holding key valye pairs """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data_r = self.get_page(page, page_size)
        t_pages = math.ceil(len(self.dataset()) / page_size)

        begin, end = index_range(page, page_size)

        # checking for the next page
        if (page < t_pages):
            n_page = page + 1
        else:
            n_page = None
        # checking out for previous page
        if (page != 1):
            pre_page = page - 1
        else:
            pre_page = None
        return {'page_size': len(data_r),
                'page': page,
                'data': data_r,
                'next_page': n_page,
                'prev_page': pre_page,
                'total_pages': t_pages
                }
