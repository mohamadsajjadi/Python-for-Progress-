import math

from person import Person, Consts


class Worker(Person):
    def __init__(self, name, age):
        super.__init__(Person)
        self.job = "worker"
        self.age = age

    def get_price(self):
        price = int(math.floor(Consts.BASE_PRICE[self.job] * Consts.MIN_AGE / self.age))
        return price

    def calc_life_cost(self):
        costs = int(math.floor(Consts.BASE_COST[self.job] * self.age / Consts.MIN_AGE))
        return costs

    def calc_income(self):
        income = int(
            math.floor(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * Consts.MIN_AGE / self.age))
        return income
