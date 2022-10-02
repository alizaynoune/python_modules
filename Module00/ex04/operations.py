import sys
# Sum: A+B
# Difference: A-B
# Product: A*B
# Quotient: A/B
# Remainder: A%B
def operations(a, b):
    result = {
        'Sum': a + b,
        'Difference': a - b,
        'Product': a * b,
        'Quotient': a / b if b else 'ERROR (division by zero)',
        'Remainder':  a % b if b else 'ERROR (modulo by zero)',
    }
    return result

if not (len(sys.argv) == 3):
    sys.exit('Usage: python3 operation.py <number1> <number2>')
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        result = operations(a, b)
        for k, v in result:
            print(k , v)
    except ValueError as e:
        sys.exit('AssertionError: %s' %e)