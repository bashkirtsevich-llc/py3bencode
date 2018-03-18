# Python 3 bencoding library
[![Build Status](https://travis-ci.org/bashkirtsevich/py3bencode.svg?branch=master)](https://travis-ci.org/bashkirtsevich/py3bencode)

Python 3 bytearray bencoding library.

Encode all data into `bytearray`. Useful for networking.

## Example

```python
from bencode import bencode, bdecode


foo = bencode({"key": [1, "2", {3: 4}})
print(foo)

bar = bdecode(foo)
print(bar)
```
