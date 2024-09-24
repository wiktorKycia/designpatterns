from abc import ABC, abstractmethod

class Warrior(ABC):
    @abstractmethod
    def fight(self):
        pass

class BowMan(ABC):
    @abstractmethod
    def shoot(self):
        pass

class Calvary(ABC):
    @abstractmethod
    def charge(self):
        pass

class PolishWarrior(Warrior):
    def fight(self):
        print("polish warrior is fighting")
class PolishBowMan(BowMan):
    def shoot(self):
        print("polish bowman is shooting")
class PolishCalvary(Calvary):
    def charge(self):
        print("polish calvary is charging")

class CzechWarrior(Warrior):
    def fight(self):
        print("czech warrior is fighting")
class CzechBowMan(BowMan):
    def shoot(self):
        print("czech bowman in shooting")
class CzechCalvary(Calvary):
    def charge(self):
        print("czech calvary is charging")