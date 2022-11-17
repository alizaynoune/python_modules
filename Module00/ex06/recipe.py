cookbook = {
    "sandwich": {
        "ingredients": ['ham', 'bread', 'cheese', 'tomatoes'],
        "meal": "lunch",
        "prep_time": 10,
    },
    "cake": {
        "ingredients": ['flour', 'sugar', 'eggs'],
        "meal": "dessert",
        "prep_time": 60,
    },
    "salad": {
        "ingredients": ['avocado', 'arugula', 'tomatoes', 'spinach'],
        "meal": "lunch",
        "prep_time": 15,
    },
}


def get_all_recipe():
    for k, v in cookbook.items():
        print('{}: {}'.format(k, v))


def get_recipe_details():
    key = input('Please enter a recipe name to get its details:\n')
    value = cookbook.get(key)
    if value:
        print('Recip for {}:\nIngredients list: {}\nTo be eaten for {}.\n\
                Takes {} minutes of cooking.'.format(key, value['ingredients'],
                                                     value['meal'],
                                                     value['prep_time']))
    else:
        print('Sorry, this recipe does not exist.')


def delete_recipe():
    key = input("Please enter recipe name:\n")
    value = cookbook.get(key)
    if value:
        print('success deleted')
        cookbook.pop(key)
    else:
        print('Sorry, this recipe does not exist')


def add_new_recip():
    name = input('Enter a name:\n')
    if not len(name):
        print('The name is requered')
        return

    ingredients = []
    print('Enter ingredients:')
    while True:
        ingre = input('')
        if len(ingre):
            ingredients.append(ingre)
        else:
            break
    mealType = input('Enter a meal type:\n')
    if not len(mealType):
        print('The Type is requered')
        return

    prep_time = input('Enter a preparation time:\n')
    if prep_time.isnumeric():
        prep_time = int(prep_time)
        if prep_time < 0:
            print('Invalid input the preparation  time is non-negative')
            return
    else:
        print("The preparation time is requered")
        return
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': mealType,
        'prep_time': prep_time
    }


def quit_app():
    print('Cookbook closed. Goodbye !')
    quit()


options = {
    '1': {
        'description': 'Add a recipe',
        'action': add_new_recip
    },
    '2': {
        'description': 'Delete a recipe',
        'action': delete_recipe
    },
    '3': {
        "description": "Print a recipe",
        "action": get_recipe_details
    },
    '4': {
        "description": "Print the cookbook",
        "action": get_all_recipe
    },
    '5': {
        "description": "Quit",
        "action": quit_app
    }
}


def print_options():
    print('List of available option:')
    for k, v in options.items():
        print('  {}: {}'.format(k, v['description']))


def run_app():
    print('Welcome to the Python Cookbook !')
    print_options()
    while True:
        selcet = options.get(input('Please select an option:\n'))
        if selcet:
            selcet['action']()
        else:
            print('Sorry, this option does not exist.')
            print_options()
        print()


run_app()
