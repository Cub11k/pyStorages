from enum import Enum


class StorageType(Enum):
    pickle = "pickle"
    json = "json"
    redis = "redis"
