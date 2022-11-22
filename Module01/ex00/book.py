from typing import Literal


class Book:
    def __init__(self, name: str, last_update, creation_date, recipes_list: Literal["starter", "lunch", "dessert"]) -> None:
        pass
    # • recipes_list (dict): a dictionnary with 3 keys: "starter", "lunch", "dessert".

    def __str__(self) -> str:
        pass
