from abc import ABC, abstractmethod
from products import *
class AbstractFactory(ABC):
    @abstractmethod
    def createWarrior(self) -> Warrior:
        pass
    @abstractmethod
    def createCalvary(self) -> Calvary:
        pass
    @abstractmethod
    def createBowMan(self) -> BowMan:
        pass

class PolishFactory(AbstractFactory):
    def createWarrior(self) -> PolishWarrior:
        return PolishWarrior()
    def createCalvary(self) -> PolishCalvary:
        return PolishCalvary()
    def createBowMan(self) -> PolishBowMan:
        return PolishBowMan()

class CzechFactory(AbstractFactory):
    def createWarrior(self) -> CzechWarrior:
        return CzechWarrior()
    def createCalvary(self) -> CzechCalvary:
        return CzechCalvary()
    def createBowMan(self) -> CzechBowMan:
        return CzechBowMan()