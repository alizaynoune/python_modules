import numpy as np


class NumPyCreator:
    def __init__(self) -> None:
        pass

    def from_list(self, lst, dtype=None):
        if not isinstance(lst, list):
            return None
        if isinstance(lst[0], list):
            lLen = len(lst[0])
            if not all(len(i) == lLen for i in lst):
                return None
        try:
            return np.array(lst, dtype)
        except Exception:
            return None

    def from_tuple(self, tpl, dtype=None):
        if not isinstance(tpl, tuple):
            return None
        if isinstance(tpl[0], tuple) and not all(
                isinstance(t, tuple) and len(t) == len(tpl[0]) for t in tpl):
            return None
        try:
            return np.array(tpl, dtype)
        except Exception:
            return None

    def from_iterable(self, itr, dtype=None):
        try:
            iter(itr)
            return np.array(itr, dtype)
        except Exception:
            return None

    def from_shape(self, shape, value=0, dtype=None):
        if not isinstance(shape, tuple) or len(shape) != 2 or not all(
                isinstance(i, int) and i >= 0 for i in shape):
            return None
        return np.full(shape, value, dtype)

    def random(self, shape):
        if not isinstance(shape, tuple) or len(shape) != 2 or not all(
                isinstance(i, int) and i >= 0 for i in shape):
            return None
        return np.random.random(shape)

    def identity(self, n, dtype=None):
        if not isinstance(n, int) or n < 0:
            return None
        return np.identity(n, dtype)
