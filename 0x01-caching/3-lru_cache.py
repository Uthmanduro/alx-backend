#!/usr/bin/env python3
"""implerments the LRUCache algorithm"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """inherits from base caching and is a caching system"""
    def __init__(self):
        """initialize the fifocache instances"""
        super().__init__()

    def put(self, key, item):
        """assign to the dict self.cache_data the item value for the key"""
        if key is None or item is None:
            return
        keys = list(self.cache_data.keys())
        if key in keys:
            self.cache_data.pop(key)
        self.cache_data.update({key: item})
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key = list(self.cache_data.keys())[0]
            self.cache_data.pop(key)
            print("DISCARD:", key)

    def get(self, key):
        """return the value in self.cache_data linked to the key"""
        val = self.cache_data.get(key)
        if val is None:
            return
        self.cache_data.pop(key)
        self.cache_data.update({key: val})
        return self.cache_data.get(key, None)
