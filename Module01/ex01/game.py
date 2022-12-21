class GotCharacter:
    """
    GotCharacter class
    """
    def __init__(self, first_name=None, is_alive=True) -> None:
        self.first_name = first_name
        self.is_alive = is_alive
        pass


class Stark(GotCharacter):
    """
    A class representing the Stark family.
    Or when bad things happen to good people.
    """

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


class Lannister(GotCharacter):
    """
    A class representing the Lannister family.
    Or when bad things happen to good people.
    """

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Winter is Over"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
