import time
import os
import functools


def logger(func):
    """
    write function logger in machine.log
    """
    @functools.wraps(func)
    def logger_wrapper(*args, **kwargs):
        Ts = time.time()
        ret = func(*args, **kwargs)
        Tt = time.time() - Ts
        fname = ' '.join(func.__name__.split('_')).title()
        exec_time = f"{Tt * 1000 if Tt < 1 else Tt :.3f} {'ms' if Tt < 1 else 's'}"
        f = open("machine.log", "a")
        f.write(
            f"({os.getlogin()})Running: {fname:19}[ exec-time = {exec_time} ]\n")
        f.close()
        return ret
    return logger_wrapper
