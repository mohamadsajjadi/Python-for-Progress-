import math

from work_place import WorkPlace, Consts


class School(WorkPlace):
    def __init__(self, name):
        super().__init__(WorkPlace)
        self.expertise = "school"

    def calc_capacity(self):
        self.capacity = int(math.floor(math.sqrt(self.level)))

    def calc_costs(self):
        costs = int(Consts.BASE_PLACE_COST * math.floor(math.sqrt(self.level)))
        return costs
