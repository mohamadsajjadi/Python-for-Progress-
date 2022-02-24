import math

from work_place import WorkPlace, Consts


class Mine(WorkPlace):
    def __init__(self, name):
        super().__init__(WorkPlace)
        self.expertise = "mine"

    def calc_capacity(self):
        self.capacity = int(math.pow(self.level, 2))

    def calc_costs(self):
        costs = int(Consts.BASE_PLACE_COST + (Consts.LEVEL_MUL * self.level))
        return costs
