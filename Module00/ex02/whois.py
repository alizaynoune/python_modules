import sys

len = len(sys.argv) - 1
if (len == 1):
    try:
        number = int(sys.argv[1])
        if not number:
            print('I\'m Zero.')
        else:
            message = 'Even' if not number % 2 else 'Odd'
            print('I\'m {0}.'.format(message))
    except ValueError:
        sys.exit('AssertionError: argument is not an integer')
    except ValueError as e:  # type: ignore
        sys.exit('AssertionError: {0}.'.format(e))

elif not (len):
    sys.exit('Usage: python whois <number>')
else:
    sys.exit('AssertionError: more than one argument are provided')
