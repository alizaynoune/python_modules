from typing import Literal


class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, description: str, recipe_type: Literal["starter", "lunch", "dessert"]) -> None:
        pass
        # recipe_type (str): can be "starter", "lunch" or "dessert".

    def __str__(self) -> str:
        pass
