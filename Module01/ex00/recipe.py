def validation(name, cooking_lvl, cooking_time, ingredients,
               description, recipe_type) -> None:
    if not name or not isinstance(name, str):
        raise ValueError('The name must be string')
    elif not isinstance(cooking_lvl, int) or not 1 <= cooking_lvl <= 5:
        raise ValueError('The cooking_lvl must be integer between 1, 5')
    elif not isinstance(cooking_time, int) or 0 > cooking_time:
        raise ValueError('The cooking_time must be a positive number')
    elif not isinstance(ingredients, list) or not ingredients or not all(
            isinstance(v, str) for v in ingredients):
        raise ValueError(
            'The ingredients must be list of all ingredients\
 each represented by a string')
    elif description and not isinstance(description, str):
        raise ValueError('The description must be string')
    elif not recipe_type or not isinstance(recipe_type, str) or recipe_type\
            not in ["starter", "lunch", "dessert"]:
        raise ValueError(
            'The recipe_type must can be "starter", "lunch" or "dessert"')


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, recipe_type, description=None) -> None:
        try:
            validation(name, cooking_lvl, cooking_time,
                       ingredients, description, recipe_type)
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
            pass
        except Exception as e:
            print(e)

    def __str__(self) -> str:
        """Return the string to print with the recipe info"""
        txt = f"name: {self.name}\ntyp: {self.recipe_type}\ncooking time: \
{self.cooking_time}m\ningredients: {self.ingredients}\ndescription: \
{self.description}"
        return txt
