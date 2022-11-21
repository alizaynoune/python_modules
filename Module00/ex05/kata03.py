kata = "The right format"
if isinstance(kata, str):
    print('{0:->42.42}'.format(kata), end='')
else:
    print('The kata is not string')
