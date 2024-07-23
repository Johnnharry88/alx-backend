#!/usr/bin/env python3
"""Module that inherits from BaseCaching
and defines function put and get"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """class that defines the puting and getting function of items from dict"""
    def __init__(self):
        """self constructor"""
        super().__init__()
        self.recentkyz = []

    def put(self, key, item):
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.recentkyz:
                self.recentkyz.append(key)
            else:
                self.recentkyz.append(
                    self.recentkyz.pop(self.recentkyz.index(key)))
            if len(self.recentkyz) > BaseCaching.MAX_ITEMS:
                rm = self.recentkyz.pop(0)
                del self.cache_data[rm]
                print('DISCARD: {}'.format(rm))

    def get(self, key):
        """returns the value stored in self.cache_data
        associated with key"""
        if key is not None and key in self.cache_data.keys():
            self.recentkyz.append(self.recentkyz.pop(self.recentkyz.index(key)))
            return self.cache_data.get(key)
        return None
