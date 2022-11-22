
def validation(name, last_update, creation_date, recipes_list) -> None:
    if not name or not isinstance(name, str):
        raise ValueError('The name must be string')
    elif not recipes_list or not isinstance(recipes_list, dict) or not recipes_list in ["starter", "lunch", "dessert"]:
        raise ValueError(
            'The recipes_list must can be "starter", "lunch" or "dessert"')


class Book:
    def __init__(self, name, last_update, creation_date, recipes_list) -> None:
        try:
            validation(name, last_update, creation_date, recipes_list)
        except Exception as e:
            print(e)
        pass
    # • recipes_list (dict): a dictionnary with 3 keys: "starter", "lunch", "dessert".

    def __str__(self) -> str:
        pass

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        # ... Your code here ...

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        # ... Your code here ...

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        # ... Your code here ...
