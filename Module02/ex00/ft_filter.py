def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
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
        if not function_to_apply:
            yield i
        else:
            if function_to_apply(i):
                yield i
