#!/usr/bin/env python3
"""
Cache module
"""


import uuid
from typing import Union, Callable, Optional
import redis
from functools import wraps


class Cache:
    """
    Cache class to interact with Redis
    """

    def __init__(self):
        """
        Initializes the Cache with a Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """ 
        increments the count in Redis every time the method is called and
        returns the value returned by the original method
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """
            implementation of wrapper function
            """
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)

        return wrapper

    @count_calls        

    @staticmethod
    def call_history(method: Callable) -> Callable:
        """
        to store the history of inputs and outputs for a particular function
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """
            implemntation of wrapper function
            """
            key = "{}:inputs".format(method.__qualname__)
            self._redis.rpush(key, str(args))

            output = method(self, *args, **kwargs)

            key = "{}:outputs".format(method.__qualname__)
            self._redis.rpush(key, str(output))

            return output

        return wrapper

    @call_history

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, stores the input data in Redis, and returns the key

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def replay(method: Callable):
        """
        to display the history of calls of a particular function
        """
        @wraps(method)
    def wrapper(*args, **kwargs):
        """
        implementation of a wrapper function
        """
        return method(*args, **kwargs)
        
        history_key = "{}:inputs".format(method.__qualname__)
        inputs = cache._redis.lrange(history_key, 0, -1)
    
        history_key = "{}:outputs".format(method.__qualname__)
        outputs = cache._redis.lrange(history_key, 0, -1)
    
        print("{} was called {} times:".format(method.__qualname__, len(inputs)))
        for input_args, output in zip(inputs, outputs):
            print("{} -> {}".format(input_args, output))

    def get(self, key: str, fn: Optional[Callable] 
            = None) -> Union[str, bytes, int, float, None]:
        """
         get method that take a key string argument and an optional
         Callable argument named fn
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        implementation of a get_str
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> Union[int, None]:
        """
        implementation of get_int
        """
        return self.get(key, fn=int)


