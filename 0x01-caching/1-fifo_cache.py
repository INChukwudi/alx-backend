#!/usr/bin/env python3

"""
Module containing the FIFOCache class
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class that defines an instance of the FIFOCache class
    Inherits from the BaseCaching class
    """
    def __init__(self):
        """
        Initialize the FIFO Cache
        """
        super().__init__()
        self.keys_queue = []


    def put(self, key, item):
        """
        Persists an item in the cache in FIFO order

        Args:
        key - identifier to store value under
        item - value to be stored
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys_queue.remove(key)
                self.cache_data[key] = item
                self.keys_queue.append(key)
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.keys_queue.pop(0)
                self.cache_data.pop(oldest_key)
                print("DISCARD: {}".format(oldest_key))
            self.cache_data[key] = item
            self.keys_queue.append(key)


    def get(self, key):
        """
        Get an item by key

        Args:
        key - identifier to look for in the cache

        Return:
        value - value stored under the key or None
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
