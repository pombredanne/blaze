from __future__ import absolute_import

"""
bparams

configuration parameters for barray
"""

class bparams(object):
    """
    bparams(clevel=5, shuffle=True, clib="blosclz", blocsize=None)

    Class to host parameters for compression and other filters.

    Parameters
    ----------
    clevel : int (0 <= clevel < 10)
        The compression level.
    shuffle : bool
        Whether the shuffle filter is active or not.
    clib : str
        The compression library to use ("blosclz", "snappy", "lz4")
    blocksize : int
        The internal blocksize used in Blosc.  If None, a default will
        be computed depending on the `clevel` value (recommended).

    Notes
    -----
    The shuffle filter may be automatically disabled in case it is
    non-sense to use it (e.g. itemsize == 1).

    """

    @property
    def clevel(self):
        """The compression level."""
        return self._clevel

    @property
    def shuffle(self):
        """Shuffle filter is active?"""
        return self._shuffle

    @property
    def clib(self):
        """Compression library to use"""
        return self._clib

    @property
    def blocksize(self):
        """The blocksize used"""
        return self._blocksize

    def __init__(self, clevel=5, shuffle=True, clib="blosclz", blocksize=None):
        if not isinstance(clevel, int):
            raise ValueError("`clevel` must an int.")
        if not isinstance(shuffle, (bool, int)):
            raise ValueError("`shuffle` must a boolean.")
        shuffle = bool(shuffle)
        if clevel < 0:
            raise ValueError("clevel must be a positive integer")
        if clib not in ("blosclz", "snappy", "lz4"):
            raise ValueError("clib '%s' is not supported." % clib)
        if blocksize is not None and not isinstance(blocksize, int):
            raise ValueError("`blocksize` must an integer.")
        self._clevel = clevel
        self._shuffle = shuffle
        self._clib = clib
        self._blocksize = blocksize

    def __repr__(self):
        args = ["clevel=%d"%self._clevel, "shuffle=%s"%self._shuffle,
                "clib=%s"%self._clib, "blocksize=%s"%self._blocksize]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(args))

## Local Variables:
## mode: python
## py-indent-offset: 4
## tab-width: 4
## fill-column: 78
