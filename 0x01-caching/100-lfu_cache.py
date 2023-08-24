#!/bin/usr/env python3

"""
Module containing the LFUCache class
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Defines an instance of the LFUCache class
    Inherits from the BaseCaching class
    """
    def __init__(self):
        """ Initialize LFU Cache """
        super().__init__()
        self.freq = {}
        self.freq_order = {}
        self.min_freq = 0

    def put(self, key, item):
        """
        Persists an item to the MRU cache

        Args:
        key - identifier to store value under
        item - value to be stored
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.freq[key] += 1
                freq = self.freq[key]

                if freq - 1 in self.freq_order:
                    self.freq_order[freq - 1].remove(key)
                    if not self.freq_order[freq - 1]:
                        self.freq_order.pop(freq - 1, None)

                self.cache_data[key] = item
                self.freq_order.setdefault(self.freq[key], []).append(key)
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                while self.min_freq in self.freq_order and \
                  len(self.freq_order[self.min_freq]) == 0:
                    self.freq_order.pop(self.min_freq)
                    self.min_freq += 1

                if self.min_freq in self.freq_order:
                    lfu_key = self.freq_order[self.min_freq].pop(0)
                    self.cache_data.pop(lfu_key)
                    print("DISCARD: {}".format(lfu_key))
            self.cache_data[key] = item
            self.freq[key] = 1
            self.freq_order.setdefault(1, []).append(key)
            self.min_freq = 1

    def get(self, key):
        """
        Get an item by key

        Args:
        key - identifier to look for in the cache

        Return:
        value - value stored under the key or None
        """
        if key is not None and key in self.cache_data:
            self.freq[key] += 1
            freq = self.freq[key]

            if freq in self.freq_order and key in self.freq_order[freq]:
                self.freq_order[freq].remove(key)

            if not self.freq_order.get(freq):
                self.freq_order.pop(freq, None)

            self.freq_order.setdefault(freq + 1, []).append(key)
            return self.cache_data[key]
        return None
