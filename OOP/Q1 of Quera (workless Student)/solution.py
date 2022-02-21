class Drug:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name):
        self.name = name
        self.drugs = list()
        self.employees = list()

    def add_drug(self, drug):
        self.drugs.append(drug)

    def add_employee(self, first_name, last_name, age):
        self.employees.append({
            "firstname": first_name,
            "lastname": last_name,
            "age": age})

    def total_value(self):
        sum = 0
        for item in self.drugs:
            sum += item.amount * item.price
        return sum

    def employees_summary(self):
        string = 'Employees:\n'
        for i in range(len(self.employees)):
            string += f"The employee number {i + 1} is {self.employees['first_name']} {self.employees['last_name']} who is {self.employees['age']} years old.\n"
        return string

# drug1 = Drug("T1", 10, 1000)
# drug2 = Drug("T2", 20, 2000)
# drug3 = Drug("T3", 30, 3000)
# drug4 = Drug("T4", 40, 4000)
# store1 = Pharmacy("S1")
# store2 = Pharmacy("S2")
# # store1.add_drug(drug1)
# # store1.add_drug(drug2)
# # store1.add_drug(drug3)
# # store1.add_drug(drug4)
# # store1.total_value()
# store1.add_employee("Seyed Ali", "Babaei", 19)
# store1.add_employee("mamad", 'sajjadi', 20)
# store1.add_employee("Seyed Ali", "Babaei", 19)
# print(store1.employees_summary())
