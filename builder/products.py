class Tank:
    def __init__(self):
        self.wheels = []
        self.tracks = None
        self.engine = None
        self.hull = None
        self.tower = None
        self.mainGun = None
    def shot(self):
        print(f'main gun of caliber {self.mainGun.caliber} shoots')
    def drive(self):
        if self.tracks is not None and self.wheels != []:
            print(f'tank is driving')
    def __str__(self):
        return f"""
        number of wheels: {len(self.wheels)},
        {"tank does have tracks" if self.tracks is not None else "tank does not have tracks"}
        engine's power: {self.engine.power}
        hull's armor: {self.hull.armor}
        tower's armor: {self.tower.armor}
        main gun's caliber: {self.mainGun.caliber}
        """