def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if not isinstance(iterable, (list, dict, tuple, set, range)):
        raise ValueError(f"'{'NoneType' if not iterable else iterable.type()}' object is not iterable")
    else:
        for i in iterable:
            if not function_to_apply:
                yield i
            else:
                if function_to_apply(i):
                    yield i


# Example 1:
# x = [1, 2, 3, 4, 5]
x = range(1, 10)
# print(ft_map(lambda dum: dum + 1, x))
try:
    print(filter(lambda dum: not (dum % 2), x))
except Exception as e:
    print(e)
try:
    print(ft_filter(lambda dum: not (dum % 2), x))
except Exception as e:
    print(e)
try:
    print(list(filter(None, x)))
except Exception as e:
    print(e)
try:
    print(list(ft_filter(None, x)))
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
