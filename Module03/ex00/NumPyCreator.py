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
            return np.asarray(lst, dtype)
        except:
            return None

    def from_tuple(self, tpl, dtype=None):
        if not isinstance(tpl, tuple):
            return None
        try:
            return np.asarray(tpl, dtype)
        except:
            return None

    def from_iterable(self, itr):
        try:
            iter(itr)
            return np.asarray(itr)
        except:
            return None

    def from_shape(self, shape, value=0):
        pass

    def random(self, shape):
        pass

    def identity(self, n):
        pass


npc = NumPyCreator()
# print(npc.from_list([1, 2, 3, 6, 4], dtype=object))
print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
# Output :
# array([[1, 2, 3], [6, 3, 4]])
print(npc.from_list([[1, 2, 3], [6, 4]]))
# # Output :
# # None
print(npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]]))
# # Output :
# # array([[’1’,’2’,’3’],
# # [’a’,’b’,’c’],
# # [’6’,’4’,’7’], dtype=’<U21’])
print(npc.from_list(((1, 2), (3, 4))))
# # Output :
# # None
print(npc.from_tuple(("a", "b", "c")))
# # Output :
# # array([’a’, ’b’, ’c’])
print(npc.from_tuple(["a", "b", "c"]))
# # Output :
# # None
print(npc.from_iterable(range(5)))
# # Output :
# # array([0, 1, 2, 3, 4])
# shape = (3, 5)
# print(npc.from_shape(shape))
# # Output :
# # array([[0, 0, 0, 0, 0],
# # [0, 0, 0, 0, 0],
# # [0, 0, 0, 0, 0]])
# print(npc.random(shape))
# # Output :
# # array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],
# # [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
# # [0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])
# print(npc.identity(4))
# # Output :
# # array([[1., 0., 0., 0.],
# # [0., 1., 0., 0.],
# # [0., 0., 1., 0.],
# # [0., 0., 0., 1.]])