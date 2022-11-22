def validation(name, cooking_lvl, cooking_time, ingredients, description, recipe_type) -> None:
    if not name or not isinstance(name, str):
        raise ValueError('The name must be string')
    elif not isinstance(cooking_lvl, int) or not 1 <= cooking_lvl <= 5:
        raise ValueError('The cooking_lvl must be integer between 1, 5')
    elif not isinstance(cooking_time, int) or 0 > cooking_time:
        raise ValueError('The cooking_time must be a positive number')
    elif not ingredients or not all(isinstance(v, str) for v in ingredients):
        raise ValueError(
            'The ingredients must be list of all ingredients each represented by a string')
    elif description and not isinstance(description, str):
        raise ValueError('The description must be string')
    elif not recipe_type or not isinstance(recipe_type, str) or not recipe_type in ["starter", "lunch", "dessert"]:
        raise ValueError(
            'The recipe_type must can be "starter", "lunch" or "dessert"')


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type) -> None:
        try:
            validation(name, cooking_lvl, cooking_time,
                       ingredients, description, recipe_type)
        except Exception as e:
            print(e)
        pass
        # recipe_type (str): can be "starter", "lunch" or "dessert".

    def __str__(self) -> str:
        pass


Recipe('test', 1, 2, ['test'], None, 'dessert')
