from factories import *

class Country:
    def __init__(self, factory: AbstractFactory):
        self.factory = factory
        self.army = [
            self.factory.createWarrior(),
            self.factory.createCalvary(),
            self.factory.createBowMan()
        ]
    def attack(self):
        self.army[0].fight()
        self.army[1].charge()
        self.army[2].shoot()

polish_factory = PolishFactory()
poland = Country(polish_factory)

czech_factory = CzechFactory()
czechia = Country(czech_factory)

poland.attack()
czechia.attack()
