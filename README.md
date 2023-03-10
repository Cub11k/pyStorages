# <p align="center">pyStorages</p>

<p align="center">Simple data storages written in Python</p>

### Currently supported storage types:
- JSON
- Pickle
- Redis

## Installation

```bash
pip install pyStorages
# or
pip install git+https://github.com/Cub11k/pyStorages.git
```

For `RedisStorage` use extras:
```bash
pip install pyStorages[redis]
# or, for async version
pip install pyStorages[aioredis]
```

## Getting started

pyStorages is the simplest way to interact with different types of storages,
where data is stored and treated as a dictionary, in terms of python -  `dict`.

Storage class interface is pretty convenient and is described below:

### Set data
```
[async] def set_data(**kwargs)
```
This method allows you to update data according to key-value pairs.
Existing key-values pairs not covered by passed keys won't be affected.

**Parameters**

`kwargs` - key-value pairs, according to which, the data will be updated

**Returns** - `None`

### Delete data
```
[async] def delete_data(*keys)
```
This method allows you to delete values by keys.

**Parameters**

`keys` - list of keys, which will be deleted, if present

**Raises** `KeyError` - in case of receiving a non-existing key

**Returns** - `None`

### Reset data
```
[async] def reset_data()
```
This method allows you to delete all data.

**Returns** - `None`

### Get data
```
[async] def get_data(*keys)
```
This method allows you to get values by keys.
For nested keys use `list`.

Note: if no keys are passed, all data will be returned.
```
>>> get_data('key1', 'key2', 'key3')
(data['key1'], data['key2'], data['key3'])

>>> get_data(['key1', 'key2'])
(data['key1']['key2'],)

>>> get_data([])
(data,)

>>> get_data()
(data,)
```

**Parameters**

`keys` - list of keys, which values will be returned, if present

**Raises** `KeyError` - in case of non-existing key

**Returns** - `tuple`

## Examples

_Coming soon..._