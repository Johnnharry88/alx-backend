#!/usr/bin/env python3
"""Module that inherits from BaseCaching
and defines function put and get"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """class that defines the puting and getting function of items from dict"""
    def __init__(self):
        """Class constructor"""
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                idx_key, idx_val = self.cache_data.popitem()
                print('DISCARD: {}'.format(idx_key))
        self.cache_data[key] = item

    def get(self, key):
        """returns the value stored in self.cache_data
        associated with key"""
        if key is None or key not in self.cache_data.keys():
            return
        return self.cache_data.get(key)
