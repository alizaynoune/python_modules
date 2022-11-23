from recipe import Recipe
from datetime import datetime


class Book:
    def __init__(self, name) -> None:
        if not name or not isinstance(name, str):
            raise ValueError('The name must be string')
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list: dict[str, list[Recipe]] = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }
        pass

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the\
 instance"""
        if not isinstance(name, str):
            raise ValueError('The recipe name must be string')
        for lst in self.recipes_list.values():
            for rec in lst:
                if rec.name == name:
                    return rec
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if not isinstance(recipe_type, str):
            raise ValueError("The recip type must be string")
        if recipe_type not in self.recipes_list:
            raise ValueError("The recip type does not exist")
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise ValueError('The recipe must be Recip instance')
        if recipe.recipe_type not in self.recipes_list:
            raise ValueError("The recip type does not exist")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
        pass
