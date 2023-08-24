#!/usr/bin/env python3

"""
Module containg the MRUCache class definition
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Defines an MRUCache class instance
    Inhertis from the BaseCaching Class
    """
    def __init__(self):
        """
        Initialize the MRUCache class instance
        """
        super().__init__()
        self.keys_mru_order = []

    def put(self, key, item):
        """
        Persists an item in the MRU cache

        Args:
        key - identifier to store value under
        item - value to be stored
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys_mru_order.remove(key)
                self.cache_data[key] = item
                self.keys_mru_order.append(key)
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.keys_mru_order.pop()
                self.cache_data.pop(mru_key)
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item
            self.keys_mru_order.append(key)

    def get(self, key):
        """
        Get an item by key

        Args:
        key - identifier to look for in the cache

        Return:
        value - value stored under the key or None
        """
        if key is not None and key in self.cache_data:
            self.keys_mru_order.remove(key)
            self.keys_mru_order.append(key)
            return self.cache_data[key]
        return None
