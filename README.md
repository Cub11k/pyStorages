# storages

Simple data storages written in Python

### Currently supported storage types:
- JSON
- Pickle
- Redis

## Installation

```bash
pip install git+https://github.com/Cub11k/storages.git
```

## Usage

```python
from storages import StorageType, load_storage

storage = load_storage(StorageType.json)

storage.set_data(
    test="test",
    test_int=5,
    test_list=[1, "2"],
    test_dict={"key1": 1, "key2": 2}
)
```