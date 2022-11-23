from book import Book
from recipe import Recipe

book_1337 = Book('mol lmsamn')

# ! error test
print('======== error tests==========\n')

try:
    Recipe('test', 2, 3, ['test'], 2)
except Exception as e:
    print(e)
try:
    Recipe('test', 2, 3, 2, 'dessert')
except Exception as e:
    print(e)

try:
    Recipe('test', 2, -3, ['test'], 'dessert')
except Exception as e:
    print(e)

try:
    Recipe('test', 10, 3, ['test'], 'dessert')
except Exception as e:
    print(e)

try:
    Recipe(None, 2, 3, ['test'], 'dessert')
except Exception as e:
    print(e)

try:
    Book([])
except Exception as e:
    print(e)

try:
    book_1337.get_recipe_by_name([])
except Exception as e:
    print(e)

try:
    if not book_1337.get_recipe_by_name('not found'):
        print('recip nout found')
except Exception as e:
    print(e)

try:
    book_1337.get_recipes_by_types([])
except Exception as e:
    print(e)

try:
    book_1337.get_recipes_by_types('not exist')
except Exception as e:
    print(e)

# * success tests
print('\n======== success tests==========\n')

sandwich = Recipe('sandwich', 2, 10, [
                  'ham', 'bread', 'cheese'], 'lunch', 'cheese sandwich')
cake = Recipe('cake', 4, 60, ['flour', 'sugar',
              'eggs'], 'dessert', 'marrocan cake')
salad = Recipe('salad', 3, 15, ['avocado', 'arugula', 'tomatoes',
               'spinach'], 'lunch', '1337 salad lkdob 3la lah 7ram')
bid_matich = Recipe('bid o maticha', 1, 10, [
                    'bid', 'maticha'], 'starter', 'ashal 2okla')

book_1337 = Book('mol lmsamn')
book_1337.add_recipe(sandwich)
book_1337.add_recipe(cake)
book_1337.add_recipe(salad)
book_1337.add_recipe(bid_matich)

for r in book_1337.get_recipes_by_types('starter'):
    rec = book_1337.get_recipe_by_name(r.name)
    print(str(rec), '\n')
for r in book_1337.get_recipes_by_types('lunch'):
    rec = book_1337.get_recipe_by_name(r.name)
    print(str(rec), '\n')
for r in book_1337.get_recipes_by_types('dessert'):
    rec = book_1337.get_recipe_by_name(r.name)
    print(str(rec))
