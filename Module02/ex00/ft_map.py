import types


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """

    if not callable(function_to_apply):
        raise ValueError(
            f"'{type(function_to_apply).__name__}' object is not callable")
    
    try:
        iter(iterable)
    except Exception as error:
        raise error
    for i in iterable:
        yield function_to_apply(i)


# Example 1:
x = range(0, 10)
# x = 2
def ft(dum): return dum + 1
# ft = None


# ft = None
try:
    print(map(ft, x))
except Exception as e:
    print(e)
try:
    print(ft_map(ft, x))
except Exception as e:
    print(e)
try:
    # print(list(map(lambda dum: dum + 1, x)))
    print(list(map(ft, x)))
except Exception as e:
    print(e)
try:
    # print(list(ft_map(lambda dum: dum + 1, x)))
    print(list(ft_map(ft, x)))
except Exception as e:
    print(e)
