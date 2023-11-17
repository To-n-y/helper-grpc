import asyncio

import aioredis

from config import REDIS_SERVER_ADDR

pos = REDIS_SERVER_ADDR.find(':')
host = REDIS_SERVER_ADDR[:pos]
port = REDIS_SERVER_ADDR[pos + 1 :]


class RedisClientEmulator:
    async def get(self, *args, **kwargs):
        return None

    async def set(self, *args, **kwargs):
        return None

    async def delete(self, *args, **kwargs):
        return None


async def get_redis_client():
    try:
        redis = await aioredis.create_redis(address=(host, port))
        return redis
    except Exception:
        return RedisClientEmulator()
