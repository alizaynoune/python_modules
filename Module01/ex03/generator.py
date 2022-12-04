from random import randrange


def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
option precise if a action is performed to the substrings before it is yielded.
    """

    if not isinstance(text, str):
        print('ERROR')
        return
    if option not in ['shuffle', 'unique', 'ordered', None]:
        print('ERROR')
        return
    if sep == '':
        yield text
        return
    lst = text.split(sep)
    if option == 'shuffle':
        for i in range(len(lst)):
            p1 = randrange(len(lst))
            lst[p1], lst[i] = lst[i], lst[p1]
    elif option == 'unique':
        lst = list(dict.fromkeys(lst))
    elif option == 'ordered':
        lst.sort()
    for w in lst:
        yield w
