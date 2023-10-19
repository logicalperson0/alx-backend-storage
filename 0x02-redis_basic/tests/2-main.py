#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
print(cache.get(cache.store.__qualname__))
cache.store(b"third")
cache.store(b"what")
print(cache.get(cache.store.__qualname__))