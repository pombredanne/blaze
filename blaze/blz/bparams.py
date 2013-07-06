from __future__ import absolute_import

"""
bparams

configuration parameters for barray
"""

class bparams(object):
    """
    bparams(clevel=5, shuffle=True, complib="blosclz")

    Class to host parameters for compression and other filters.

    Parameters
    ----------
    clevel : int (0 <= clevel < 10)
        The compression level.
    shuffle : bool
        Whether the shuffle filter is active or not.
    complib : str
        The compression library to use ("blosclz", "snappy", "lz4")

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
    def complib(self):
        """Compression library to use"""
        return self._complib

    def __init__(self, clevel=5, shuffle=True, complib="blosclz"):
        if not isinstance(clevel, int):
            raise ValueError("`clevel` must an int.")
        if not isinstance(shuffle, (bool, int)):
            raise ValueError("`shuffle` must a boolean.")
        shuffle = bool(shuffle)
        if clevel < 0:
            raise ValueError("clevel must be a positive integer")
        if complib not in ("blosclz", "snappy", "lz4"):
            raise ValueError("complib '%s' is not supported." % complib)
        self._clevel = clevel
        self._shuffle = shuffle
        self._complib = complib

    def __repr__(self):
        args = ["clevel=%d"%self._clevel, "shuffle=%s"%self._shuffle,
                "complib=%s"%self._complib]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(args))

## Local Variables:
## mode: python
## py-indent-offset: 4
## tab-width: 4
## fill-column: 78
