from functools import reduce


def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if not isinstance(iterable, (list, dict, tuple, set, range)):
        raise ValueError(
            f"'{'NoneType' if not iterable else iterable.type()}' object is not iterable")
    else:
        lst = None
        prev, next = None, iter(iterable)
        # print(next.__next__())
        while True:
            try:
                t = (next.__next__())
                lst = function_to_apply('' if not lst else lst, t)
                print(lst)
                # prev = t
                yield lst
                # print(t, prev)
            except StopIteration:
                break
        # for i in iterable:
        #     # prev = iterable.__iter.next()
        #     yield function_to_apply('', i)


# Example 1:
# x = [1, 2, 3, 4, 5]
# x = ["H", "e", "l", "l", "o", " ""w", "o", "r", "l", "d"]
# # print(ft_map(lambda dum: dum + 1, x))
# try:
#     print(reduce(lambda u, v: u + v, x))
# except Exception as e:
#     print(e)
# # try:
# #     print(ft_reduce(lambda u, v: u + v, x))
# # except Exception as e:
# #     print(e)
# try:
#     print(list(reduce(lambda u, v: u + v, x)))
# except Exception as e:
#     print(e)
# try:
#     print(list(ft_reduce(lambda u, v: u + v, x)))
# except Exception as e:
#     print(e)
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
lst = ["H", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
st = ft_reduce(lambda u, v: u + v, lst)
print(list(st), str(st))
# # Output:
# "Hello world"
