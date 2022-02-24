from person import Person, Consts


class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(Person)
        self.job = "teacher"
        self.age = age

    def get_price(self):
        price = int(Consts.BASE_PRICE[self.job] - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL)
        return price

    def calc_life_cost(self):
        costs = int(Consts.BASE_COST[self.job] + (self.age - Consts.MIN_AGE) * Consts.AGE_MUL)
        return costs

    def calc_income(self):
        income = int(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()]-(self.age-Consts.MIN_AGE)*Consts.AGE_MUL)
        return income
