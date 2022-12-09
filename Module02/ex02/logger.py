import time
from random import randint
import os
import functools


def log(func):
    @functools.wraps(func)
    def logger_wrapper(*args, **kwargs):
        Ts = time.time()
        ret = func(*args, **kwargs)
        Tt = time.time() - Ts
        fn = ' '.join(func.__name__.split('_')).title()
        e_t = f"{Tt * 1000 if Tt < 1 else Tt :.3f} {'ms' if Tt < 1 else 's'}"
        f = open("machine.log", "a")
        f.write(
            f"({os.environ['USER']})Running: {fn:19}[ exec-time = {e_t} ]\n")
        f.close()
        return ret
    return logger_wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
