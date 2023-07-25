#!/usr/bin/env python3
""" Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a cahing system that inherits from basecaching class"""
    def __init__(self):
        """initialize the instances"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the key"""
        if key is None or item is None:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """return the value in self.cache_data linked to the key"""
        return self.cache_data.get(key)
