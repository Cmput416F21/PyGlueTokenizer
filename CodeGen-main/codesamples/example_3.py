class HilbertSpace(Basic):
    """An abstract Hilbert space for quantum mechanics.
    In short, a Hilbert space is an abstract vector space that is complete
    with inner products defined [1]_.
    Examples
    ========
    >>> from sympy.physics.quantum.hilbert import HilbertSpace
    >>> hs = HilbertSpace()
    >>> hs
    H
    References
    ==========
    .. [1] https://en.wikipedia.org/wiki/Hilbert_space
    """

    def __new__(cls):
        obj = Basic.__new__(cls)
        return obj

