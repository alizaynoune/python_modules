import sys

if (len(sys.argv) > 1):
    str = " ".join([i.swapcase()[::-1] for i in sys.argv[::-1][:-1]])
    print(str)
else:
    print('Please enter at least one argument')
