"""cache.py"""

import asyncio
import os
from datetime import timedelta
from functools import partial, update_wrapper, wraps
from http import HTTPStatus
from typing import Union

from fastapi import Response

from cache.client import Cache
from cache.util import (
    ONE_DAY_IN_SECONDS,
    ONE_HOUR_IN_SECONDS,
    ONE_MONTH_IN_SECONDS,
    ONE_WEEK_IN_SECONDS,
    ONE_YEAR_IN_SECONDS,
    deserialize_json,
    serialize_json,
)


def cache(
    *,
    namespace: str | None = None,
    expire: int | timedelta = ONE_YEAR_IN_SECONDS
):
    """Enable caching behavior for the decorated function.

    Args:
        expire (Union[int, timedelta], optional): The number of seconds
            from now when the cached response should expire. Defaults to 31,536,000
            seconds (i.e., the number of seconds in one year).
        namespace (str|None, optional): cache namespace for expiration usage
    """

    def outer_wrapper(func):
        @wraps(func)
        async def inner_wrapper(*args, **kwargs):
            """Return cached value if one exists, otherwise evaluate the wrapped function and cache the result."""

            func_kwargs = kwargs.copy()
            request = func_kwargs.pop("request", None)
            response = func_kwargs.pop("response", None)
            create_response_directly = not response
            if create_response_directly:
                response = Response()
            redis_cache = Cache()
            if (
                redis_cache.not_connected
                or redis_cache.request_is_not_cacheable(request)
            ):
                # if the redis client is not connected or request is not cacheable, no caching behavior is performed.
                return await get_api_response_async(func, *args, **kwargs)
            key = redis_cache.get_cache_key(func, namespace, *args, **kwargs)
            ttl, in_cache = await redis_cache.check_cache(key)
            if in_cache:
                return deserialize_json(in_cache)
                redis_cache.set_response_headers(
                    response, True, deserialize_json(in_cache), ttl
                )
                if redis_cache.requested_resource_not_modified(
                    request, in_cache
                ):
                    response.status_code = int(HTTPStatus.NOT_MODIFIED)
                    return (
                        Response(
                            content=None,
                            status_code=response.status_code,
                            media_type="application/json",
                            headers=response.headers,
                        )
                        if create_response_directly
                        else response
                    )
                return (
                    Response(
                        content=in_cache,
                        media_type="application/json",
                        headers=response.headers,
                    )
                    if create_response_directly
                    else deserialize_json(in_cache)
                )
            response_data = await get_api_response_async(func, *args, **kwargs)
            ttl = calculate_ttl(expire)

            cached = await redis_cache.add_to_cache(key, response_data, ttl)
            return response_data
            if cached:
                redis_cache.set_response_headers(
                    response,
                    cache_hit=False,
                    response_data=response_data,
                    ttl=ttl,
                )
                return (
                    Response(
                        content=serialize_json(response_data),
                        media_type="application/json",
                        headers=response.headers,
                    )
                    if create_response_directly
                    else response_data
                )
            return response_data

        return inner_wrapper

    return outer_wrapper


def invalidate(*, namespace: str | None = None):
    """Enable cache invalidating behavior for the decorated function.

    Args:
        namespace (str|None, optional): cache namespace for expiration usage
    """

    def outer_wrapper(func):
        @wraps(func)
        async def inner_wrapper(*args, **kwargs):
            """delete cached namespace."""
            redis_cache = Cache()
            if redis_cache.connected:
                # if the redis client is not connected no caching behavior is performed.
                pattern = redis_cache.get_cache_key_pattern(namespace)
                await redis_cache.invalidate(pattern)
            return await get_api_response_async(func, *args, **kwargs)

        return inner_wrapper

    return outer_wrapper


async def get_api_response_async(func, *args, **kwargs):
    """Helper function that allows decorator to work with both async and non-async functions."""
    return (
        await func(*args, **kwargs)
        if asyncio.iscoroutinefunction(func)
        else func(*args, **kwargs)
    )


def calculate_ttl(expire: Union[int, timedelta]) -> int:
    """ "Converts expire time to total seconds and ensures that ttl is capped at one year."""
    if isinstance(expire, timedelta):
        expire = int(expire.total_seconds())
    return min(expire, ONE_YEAR_IN_SECONDS)


def nocache(*args, **kwargs):
    """dummy decorator for replacing cache decorator when caching is disabled"""

    def decorator(func):
        return func

    return decorator


cache_one_minute = partial(cache, expire=60)
cache_one_hour = partial(cache, expire=ONE_HOUR_IN_SECONDS)
cache_one_day = partial(cache, expire=ONE_DAY_IN_SECONDS)
cache_one_week = partial(cache, expire=ONE_WEEK_IN_SECONDS)
cache_one_month = partial(cache, expire=ONE_MONTH_IN_SECONDS)
cache_one_year = partial(cache, expire=ONE_YEAR_IN_SECONDS)

update_wrapper(cache_one_minute, cache)
update_wrapper(cache_one_hour, cache)
update_wrapper(cache_one_day, cache)
update_wrapper(cache_one_week, cache)
update_wrapper(cache_one_month, cache)
update_wrapper(cache_one_year, cache)


caching = os.getenv("CACHING")
caching_disable = caching is not None and caching.lower() in ["false", "False"]
if caching_disable:
    cache = nocache
else:
    cache = cache
