#!/usr/bin/env python3
"""implemtnets the LIFOCache class"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherits from base caching and is a caching system"""
    def __init__(self):
        """initialize the fifocache instances"""
        super().__init__()

    def put(self, key, item):
        """assign to the dict self.cache_data the item value for the key"""
        if key is None or item is None:
            return
        if len(self.cache_data) > 1:
            last_key = list(self.cache_data.keys())[-1]
        self.cache_data.update({key: item})
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
#            last_key = list(self.cache_data.keys())[-1]
            self.cache_data.pop(last_key)
            print("DISCARD:", last_key)

    def get(self, key):
        """return the value in self.cache_data linked to the key"""
        return self.cache_data.get(key)
