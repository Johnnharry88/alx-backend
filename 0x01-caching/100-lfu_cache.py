#!/usr/bin/env python3
"""Module holding function that returns
least frequently used cache"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Class LFU"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.reorder = []
        self.arranged = {}

    def put(self, key, item):
        """Adds items to the cache system"""
        if key is None or item is None:
            pass
        else:
            n = len(self.cache_data)
            if n >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                least = min(self.arranged.values())
                l_kyz = []
                for x, y in self.arranged.items():
                    if y == least:
                        l_kyz.append(x)
                if len(l_kyz) > 1:
                    lfu_lru = {}
                    for x in l_kyz:
                        lfu_lru[x] = self.reorder.index(x)
                    rem = min(lfu_lru.values())
                    rem = self.reorder[rem]
                else:
                    rem = l_kyz[0]

                print('DISCARD: {}'.format(rem))
                del self.cache_data[rem]
                del self.reorder[self.reorder.index(rem)]
                del self.arranged[rem]
            if key in self.arranged:
                self.arranged[key] += 1
            else:
                self.arranged[key] = 1
            if key in self.reorder:
                del self.reorder[self.reorder.index(key)]
            self.reorder.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets data from the cache with key"""
        if key is not None and key in self.cache_data:
            del self.reorder[self.reorder.index(key)]
            self.reorder.append(key)
            self.arranged[key] += 1
            return self.cache_data.get(key)
        return None
