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

    if not isinstance(function_to_apply, types.FunctionType):
        raise ValueError(
            f"'{'NoneType' if not function_to_apply else function_to_apply.type() }' object is not callable")

    if not isinstance(iterable, (list, dict, tuple, set, range)):
        raise ValueError(f"'{'NoneType' if not iterable else iterable.type()}' object is not iterable")
    else:
        for i in iterable:
            yield function_to_apply(i)


# Example 1:
x = range(0, 10)
# print(ft_map(lambda dum: dum + 1, x))
try:
    print(map(lambda dum: dum + 1, x))
except Exception as e:
    print(e)
try:
    print(ft_map(lambda dum: dum + 1, x))
except Exception as e:
    print(e)
try:
    # print(list(map(lambda dum: dum + 1, x)))
    print(list(map(lambda dum: dum + 1, None)))
except Exception as e:
    print(e)
try:
    # print(list(ft_map(lambda dum: dum + 1, x)))
    print(list(ft_map(lambda dum: dum + 1, None)))
except Exception as e:
    print(e)
# print(map(20, 20))
# Output:
# print(list(ft_map(lambda t: t + 1, x)))
# print(list(map(lambda t: t + 1, x)))
# # Output:
# [2, 3, 4, 5, 6]
# # Example 2:
# ft_filter(lambda dum: not (dum % 2), x)
# # Output:
# list(ft_filter(lambda dum: not (dum % 2), x))
# # Output:
# [2, 4]
# # Example 3:
# lst = [’H’, ’e’, ’l’, ’l’, ’o’, ’ ’, ’w’, ’o’, ’r’, ’l’, ’d’]
# ft_reduce(lambda u, v: u + v, lst)
# # Output:
# "Hello world"
