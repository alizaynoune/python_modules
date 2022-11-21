from pydoc import stripid
import sys

if (len(sys.argv) > 1):
    lst = ' '.join(
        filter(None, [i.swapcase()[::-1] for i in sys.argv[::-1][:-1]]))
    print(lst)
else:
    print('Usage: python exec \'Hello World!\'')
