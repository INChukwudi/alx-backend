#!/usr/bin/env python3
"""
Module containing the LRUCache class
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Defines an instance of the LRUCache class
    inherits from the BaseCaching class
    """
    def __init__(self):
        """
        Initialize LRU Cache class instance
        """
        super().__init__()
        self.keys_lru_order = []

    def put(self, key, item):
        """
        Persists an item in the LRU cache

        Args:
        key - identifier to store value under
        item - value to be stored
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys_lru_order.remove(key)
                self.cache_data[key] = item
                self.keys_lru_order.append(key)
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.keys_lru_order.pop(0)
                self.cache_data.pop(lru_key)
                print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item
            self.keys_lru_order.append(key)

    def get(self, key):
        """
        Get an item by key

        Args:
        key - identifier to look for in the cache

        Return:
        value - value stored under the key or None
        """
        if key is not None and key in self.cache_data:
            self.keys_lru_order.remove(key)
            self.keys_lru_order.append(key)
            return self.cache_data[key]
        return None
