from work_place import WorkPlace, Consts


class Company(WorkPlace):
    def __init__(self, name):
        super().__init__(WorkPlace)
        self.expertise = "company"

    def calc_capacity(self):
        self.capacity = int(self.level)

    def calc_costs(self):
        costs = int(Consts.BASE_PLACE_COST * self.level)
        return costs
