from enum import Enum
from typing import Union

from storages import sync_storages
from storages import async_storages


class StorageType(Enum):
    pickle = "pickle"
    json = "json"
    redis = "redis"


Storage = Union[
    sync_storages.PickleStorage, sync_storages.JSONStorage, sync_storages.RedisStorage,
    async_storages.PickleStorage, async_storages.JSONStorage, async_storages.RedisStorage,
]

__all__ = (
    "Storage",
    "StorageType",
    "sync_storages", "async_storages"
)
