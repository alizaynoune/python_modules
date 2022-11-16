kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

if isinstance(kata, dict):
    if all(isinstance(v, str) for v in kata) and len(kata):
        for k, v in kata.items():
            print('{} was created by {}'.format(k, v))
    elif not len(kata):
        print('The kata is empty')
    else:
        print("The kata don't contain all strings")
else:
    print('The kata is not dictionary')
