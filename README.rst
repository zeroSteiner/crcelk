CrcElk
======

|Github Issues| |PyPi Release|

CrcElk is an updated fork of the `CrcMoose <http://www.nightmare.com/~ryb/>`__
module for recent versions of Python. It provides a pure Python implementation
of the CRC algorithm and allows for variants to easily be defined by providing
their parameters such as width, starting polynomial, etc. Python versions 2.6+
and 3.1+ are supported.

Usage Example
-------------

.. code:: python

    >>> import crcelk
    >>> import struct
    >>> crc = crcelk.CRC_CCITT.calc_bytes(b'Hello World')
    >>> print("{0} (0x{0:04x})".format(crc))
    19749 (0x4d25)

License
-------

CrcElk is released under the same MIT license as the original CrcMoose
source. Details are available in the `file
header <https://github.com/zeroSteiner/crcelk/blob/master/crcelk.py#L4-L24>`__.

.. |Github Issues| image:: http://img.shields.io/github/issues/zerosteiner/crcelk.svg?style=flat-square
   :target: https://github.com/zerosteiner/crcelk/issues
.. |PyPi Release| image:: https://img.shields.io/pypi/v/crcelk.svg?style=flat-square
   :target: https://pypi.python.org/pypi/crcelk
