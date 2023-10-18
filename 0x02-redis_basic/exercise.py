#!/usr/bin/env python3
"""
contians a Cache class defn for redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """Redis client as a private variable named _redis (using redis.Redis())
    and flush the instance using flushdb"""
    def __init__(self) -> None:
        """init a Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that takes a data argument and returns a string"""
        ran_key = str(uuid.uuid4())
        self._redis.set(ran_key, data)
        return ran_key
