from enum import Enum
from typing import Union

from storages import sync_storages
from storages import async_storages


class StorageType(Enum):
    pickle = "pickle"
    json = "json"
    redis = "redis"


__all__ = (
    "StorageType",
    "sync_storages", "async_storages"
)
