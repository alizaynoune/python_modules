from os import get_terminal_size
from time import time


def ft_progress(listy: range):
    columns = get_terminal_size().columns - 60
    time_start = time()
    for i in listy:
        elapsed_time = time() - time_start
        percent = (i + 1) / listy.stop
        print('ETA: {:.2f}s [{:3.0f}%][{:{}.{}}] {}/{} | elapsed time {:.2f}s'.
              format(((elapsed_time / (percent * 100)) * 100) - elapsed_time,
                     (percent * 100), ('=' * round(percent * (columns))) + '>',
                     columns, columns, i + 1, listy.stop, elapsed_time),
              end='\r')
        yield i
