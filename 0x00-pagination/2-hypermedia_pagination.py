#!/usr/bin/env python3
"""implements a simple pagination"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size 2"""
    return (((page_size * page) - page_size), (page_size * page))


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
        """return the appropriate page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int) and\
            page_size > 0 and page > 0
        start, stop = index_range(page, page_size)
        try:
            dataset = self.dataset()
            return dataset[start: stop]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """return the appropriate page of the dataset"""
        total_page = math.ceil(len(self.dataset()) / page_size)
        return_dict = {}
        data = self.get_page(page, page_size)
        page_size = len(data)
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_page else None
        return_dict = {"page_size": page_size, "page": page, "data": data,
                       "next_page": next_page, "prev_page": prev_page,
                       "total_pages": total_page}
        return return_dict
