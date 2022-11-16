kata = (19, 42, 21)
if isinstance(kata, tuple):
    if all(isinstance(v, int) for v in kata) and len(kata):
        print('The {0} are: {1}'.format(len(kata),
                                        ', '.join([str(n) for n in kata])))
    elif not len(kata):
        print("The kata is empty")
    else:
        print("The kata don't contain all integers")

else:
    print('The kata is not tuple')
