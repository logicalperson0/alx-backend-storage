#!/usr/bin/env python3
"""
contians a Cache class defn for redis
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """a decorator that takes a single method Callable argument"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """a wrapper method that will incr in redis the method arg"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """Redis client as a private variable named _redis (using redis.Redis())
    and flush the instance using flushdb"""
    def __init__(self) -> None:
        """init a Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that takes a data argument and returns a string"""
        ran_key = str(uuid.uuid4())
        self._redis.set(ran_key, data)
        return ran_key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """This callable will be used to convert the data back
        to the desired format"""
        get_key = self._redis.get(key)

        if not get_key:
            return
        if get_key is not None and callable(fn):
            return fn(get_key)
        return get_key

    def get_str(self, key: str) -> str:
        """return: string of data in key"""
        get_key = self.get(str(key))

        return get_key

    def get_int(self, key: str) -> int:
        """return int of data in key"""
        get_keyi = self.get(int(key))

        return get_keyi
