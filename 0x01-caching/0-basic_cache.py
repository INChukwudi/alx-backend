#!/usr/bin/env python3

"""
Modulee containing the BasicCache class
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    The BasicCache class inheriting from BasicCaching
    """
    def put(self, key, item):
        """
        Persists an item in the cache

        Args:
        key - the identifier
        item - the value to be stored
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key

        Args:
        key - the identifier to fetch its value

        Return:
        value - the item in the cache under the key or None
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
