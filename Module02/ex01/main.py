def what_are_the_vars(*args, **kwargs):
    """
    setattr from *args, **kwargs to ObjectC instance
    @Return obj if success else None
    """
    obj = ObjectC()
    for k, v in enumerate(args):
        setattr(obj, f'var_{k}', v)

    for (k, v) in kwargs.items():
        if hasattr(obj, k):
            return None
        setattr(obj, k, v)
    return obj


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
    else:
        for attr in dir(obj):
            if attr[0] != '_':
                value = getattr(obj, attr)
                print("{}: {}".format(attr, value))
    print("end")
