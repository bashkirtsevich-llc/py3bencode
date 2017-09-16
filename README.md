# Python 3 bencoding library

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