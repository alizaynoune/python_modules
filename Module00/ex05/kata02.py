kata = (2019, 9, 25, 3, 30)

if isinstance(kata, tuple):
    if len(kata) >= 5:
        if all(isinstance(v, int) for v in kata):
            print('{0:02}/{1:02}/{2} {3:02}:{4:02}'.format(
                kata[1], kata[2], kata[0], kata[3], kata[4]))
        else:
            print("The kata don't contain all integers")
    elif not len(kata):
        print('The kata is empty')
else:
    print('The kata is not tuple')
