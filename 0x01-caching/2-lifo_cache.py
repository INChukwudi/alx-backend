#!/usr/bin/env python3

"""
Module containing the LIFOCache Class
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Defines the LIFOCache class instance
    Inherits from the BaseCaching Class
    """
    def __init__(self):
        """
        Initialize the LIFOCache Class"""
        super().__init__()
        self.keys_stack = []

    def put(self, key, item):
        """
        Persists an item in the LIFO cache

        Args:
        key - identifier to store value under
        item - value to be stored
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys_stack.remove(key)
                self.cache_data[key] = item
                self.keys_stack.append(key)
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                recent_key = self.keys_stack.pop()
                self.cache_data.pop(recent_key)
                print("DISCARD: {}".format(recent_key))
            self.cache_data[key] = item
            self.keys_stack.append(key)

    def get(self, key):
        """
        Get an item from the LIFO cache by key

        Args:
        key - identifier to look for in the cache

        Return:
        value - value stored under the key or None
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
