#!/usr/bin/env python3
""" A fucntion that takes two arguents of integer and  returns a tuple """


from typing import Dict, List
import math
import csv


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Indexing dataset by sortiing position starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_database = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
                    }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """Returns indexed data matching input index"""
        if index is None:
            index = 0

        # checks out for the indes values
        assert isinstance(index, int)
        assert 0 <= index < len(self.indexed_dataset())
        assert isinstance(page_size, int) and page_size > 0

        d_x = []
        next_idx = index + page_size

        for x in range(index, next_idx):
            if self.indexed_dataset().get(x):
                d_x.append(self.indexed_dataset()[x])
            else:
                x = x + 1
                next_idx += 1
        return {
            'index': index,
            'data': d_x,
            'page_size': page_size,
            'next_index': next_idx
            }
