import redis
from threading import Lock
from config import settings


class RedisClient:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(RedisClient, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "pool"):
            self.pool = redis.ConnectionPool(
                host=settings.Redis.host,
                port=6379,
                charset="utf-8",
                decode_responses=True,
            )

    def get_client(self):
        return redis.Redis(connection_pool=self.pool)
