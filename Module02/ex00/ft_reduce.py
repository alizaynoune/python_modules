from functools import reduce
import types


def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """

    if not callable(function_to_apply):
        raise ValueError(
            f"'{type(function_to_apply).__name__}' object is not callable")
    try:
        next = iter(iterable)
        if not len(iterable):
            raise ValueError(
                "ft_reduce() of empty sequence with no initial value")
        ret = next.__next__()
    except Exception as error:
        raise error
    while True:
        try:
            i = next.__next__()
            ret = function_to_apply(ret, i)
        except StopIteration:
            break
    return ret


lst = ["H", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
# lst = None
def ft(u, v): return u + v
ft = None


try:
    print(reduce(ft, lst))
except Exception as e:
    print(e)
try:
    print(ft_reduce(ft, lst))
except Exception as e:
    print(e)
