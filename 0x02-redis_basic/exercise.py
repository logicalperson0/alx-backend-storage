#!/usr/bin/env python3
"""
contians a Cache class defn for redis
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable])\
            -> Union[str, bytes, int, float]:
        """This callable will be used to convert the data back
        to the desired format"""
        get_key = self._redis.get(key)

        if get_key is not None and fn is callable:
            return fn(get_key)
        return get_key

    def get_str(self, key: str) -> str:
        """return: string of data in key"""
        get_key = self.get(key, fn=lambda d: d.decode('utf-8'))

        return get_key

    def get_int(self, key: str) -> int:
        """return int of data in key"""
        get_keyi = self.get(key, fn=int)

        return get_keyi
