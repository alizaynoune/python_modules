kata = (0, 4, 132.42222, 10000, 12345.67)


def is_dicemal(v):
    return isinstance(v, int) or isinstance(v, float)


if isinstance(kata, tuple):
    if len(kata) == 5:
        if all(
                isinstance(kata[x], int) and 0 <= kata[x] < 100
                for x in range(2)) and is_dicemal(kata[2]) and is_dicemal(
                    kata[4]) and isinstance(kata[3], int):
            print(
                'module_{0:02}, ex_{1:02} : {2:.2f}, {3:.2e}, {4:.2e}'.format(
                    kata[0], kata[1], kata[2], kata[3], kata[4]))
        else:
            print('please make sure the kata contain (<non-negative integer>, \
                    <non-negative integer>, <decimal>, <integer>, <decimal>)')
    else:
        print('The kata lenght is not 5')
else:
    print('The kata is not tuple')
