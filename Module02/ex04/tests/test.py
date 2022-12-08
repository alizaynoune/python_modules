from random import randint
import time
from my_minipack import progressbar, logger


class CoffeeMachine():
    water_level = 100

    @logger
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @logger
    def boil_water(self):
        return "boiling..."

    @logger
    def make_coffee(self):
        if self.start_machine():
            print(self.boil_water())
            for _ in progressbar(range(20)):
                time.sleep(0.1)
                self.water_level -= 1
            print()
            print("Coffee is ready!")

    @logger
    def add_water(self, water_level):
        r = randint(1, 5)
        for _ in progressbar(range(r * 100)):
            time.sleep(r / 100)
        self.water_level += water_level
        print()
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
