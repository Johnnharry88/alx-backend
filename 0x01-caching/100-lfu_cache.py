#!/usr/bin/env python3
"""Module holding function that returns
least frequently used cache"""
from base_caching import BaseCaching
from collections import OrderedDict
import operator


class LFUCache(BaseCaching):
    """Class LFU"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.reorder = OrderedDict()
        self.arranged = None

    def put(self, key, item):
        """Places items in cache system"""
        if key is None or item is None:
            return
        if len(self.cache_data) > self.MAX_ITEMS and key not in self.reorder:
            self.arranged = sorted(self.reorder.items(), key=operator.itemgetter(1))
            rm = self.arranged.pop(0)[0]
            del self.reorder[rm]
            del self.cache_data[rm]
            print('DISCARD: {}'.format(rm))

        if key and item:
            val = 0
            if key in self.cache_data:
                val = self.reorder[key]
                del self.reorder[key]
            self.reorder[key] = val + 1
            self.cache_data[key] = item

    def get(self, key):
        """Gets data from the cache with key"""
        return self.cache_data.get(key) 

