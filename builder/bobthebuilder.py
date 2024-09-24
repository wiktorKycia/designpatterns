from abc import ABC, abstractmethod
from subproducts import *
from products import *
class TankBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass
    @abstractmethod
    def buildHull(self):
        pass
    @abstractmethod
    def buildTracks(self):
        pass
    @abstractmethod
    def buildEngine(self):
        pass
    @abstractmethod
    def buildWheels(self, number):
        pass
    @abstractmethod
    def buildTower(self):
        pass
    @abstractmethod
    def buildMainGun(self):
        pass

class TankBuilder1(TankBuilder):
    def __init__(self):
        self._tank : Tank | None= None
        self.reset()
    def reset(self):
        self._tank = Tank()

    def buildHull(self):
        self._tank.hull = Hull(15)

    def buildTracks(self):
        self._tank.tracks = Tracks(10)

    def buildEngine(self):
        self._tank.engine = Engine(2500, 120)

    def buildWheels(self, number):
        for i in range(number):
            self._tank.wheels.append(Wheel(20))
    def buildTower(self):
        self._tank.tower = Tower(40)
    def buildMainGun(self):
        self._tank.mainGun = MainGun(31)
    def getResult(self):
        tank = self._tank
        self._tank = None
        self.reset()
        return tank

class Director:
    def constructLightTank(self, builder : TankBuilder):
        builder.reset()
        builder.buildHull()
        builder.buildEngine()
        builder.buildWheels(8)
        builder.buildTower()
        builder.buildMainGun()
    def constructHeavyTank(self, builder : TankBuilder):
        builder.reset()
        builder.buildHull()
        builder.buildEngine()
        builder.buildTracks()
        builder.buildTower()
        builder.buildMainGun()

if __name__ == '__main__':
    director = Director()
    tankbuilder = TankBuilder1()
    director.constructLightTank(tankbuilder)
    tank:Tank = tankbuilder.getResult()

    director.constructHeavyTank(tankbuilder)
    tank2:Tank = tankbuilder.getResult()

    print(tank)
    print(tank2)