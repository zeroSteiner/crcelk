# CrcElk
[![Github Issues](http://img.shields.io/github/issues/zerosteiner/crcelk.svg?style=flat-square)](https://github.com/zerosteiner/crcelk/issues)
[![PyPi Release](https://img.shields.io/pypi/v/crcelk.svg?style=flat-square)](https://pypi.python.org/pypi/crcelk)

This is an updated fork of the [CrcMoose][1] module
for recent versions of Python. Python versions 2.6+ and 3.1+ are supported.

## Usage Example
```python
>>> import crcelk
>>> import struct
>>> crc = crcelk.CRC_CCITT.calc_bytes(b'Hello World')
>>> print("{0} (0x{0:04x})".format(crc))
19749 (0x4d25)
```

## License
CrcElk is released under the same MIT license as the original CrcMoose source.
Details are available in the [file header][2].

[1]: http://www.nightmare.com/~ryb/
[2]: https://github.com/zeroSteiner/crcelk/blob/master/crcelk.py#L4-L24
