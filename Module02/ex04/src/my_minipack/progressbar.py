from os import get_terminal_size
from time import time


def progressbar(listy: range):
    """
    show bar progressbar similar tqdm 
    """
    columns = get_terminal_size().columns - 60
    time_start = time()
    end = listy.stop - listy.start
    new_rang = range(0, end, listy.step)
    for i in new_rang:
        elapsed_time = time() - time_start
        percent = (abs(i) + 1) / abs(end)
        print('ETA: {:.2f}s [{:3.0f}%][{:{}.{}}] {}/{} | elapsed time {:.2f}s'.
              format(((elapsed_time / (percent * 100)) * 100) - elapsed_time,
                     (percent * 100), ('=' * round(percent * (columns))) + '>',
                     columns, columns,
                     abs(i) + 1, abs(end), elapsed_time),
              end='\r')
        yield i
