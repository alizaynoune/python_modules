import sys

if (len(sys.argv) > 1):
    list = sys.argv[::-1][:-1]
    for str in list:
        print(str[::-1].swapcase(), end=' ' if str != list[-1] else '\n')

else:
    print('Please enter at least one argument')
