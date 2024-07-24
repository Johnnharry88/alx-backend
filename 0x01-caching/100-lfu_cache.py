#!/usr/bin/env python3
"""Module holding function that returns
least frequently used cache"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """Class LFU"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.reorder = OrderedDict()
        self.arranged = []

    def render_reorder(self, r_ukeyx):
        """Rearranges the items in the cache based on
        recentely used item"""
        mx_pos = []
        r_ufreq = 0
        r_upos = 0
        i_pos = 0
        for x,  y in enumerate(self.arranged):
            if y[0] == r_ufreq:
                r_ufreq = y[1] + 1
                r_upos = x
                break
            elif len(mx_pos) == 0:
                mx_pos.append(x)
            elif y[1] < self.arranged[mx_pos[-1]][1]:
                mx_pos.append(x)
        mx_pos.reverse()
        for p in mx_pos:
            if self.arranged[p][1] > r_ufreq:
                break
            i_pos = p
        self.arranged.pop(r_upos)
        self.arranged.insert(i_pos, [r_ukeyx, r_ufreq])

    def put(self, key, item):
        """Places items in cache system"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_fkyz, _ = self.arranged[-1]
                self.cache_data.pop(least_fkyz)
                self.arranged.pop()
                print('DISCARD: {}'.format(least_fkyz))
            self.cache_data[key] = item
            i_index = len(self.arranged)
            for x, y in enumerate(self.arranged):
                if y[1] == 0:
                    i_index = x
                    break
            self.arranged.insert(i_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.render_reorder(key)

    def get(self, key):
        """Gets data from the cache with key"""
        if key is not None and key in self.cache_data:
            self.render_reorder(key)
        return self.cache_data.get(key, None)
