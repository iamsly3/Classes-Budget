class Category:

    def __init__(self, food, clothing = 500, carExpense = 200, amount =1000):
        self.food = food
        self.clothing = clothing
        self.carExpense = carExpense
        self.amount = amount


    #methods
    def deposit(self):
        self.food = 20
        return "This is a deposit method"

    def check_balance(self):
        pass

    def withdrawl(self):
        pass

    def transfer(self):
        pass



food = Category("groceries", 1000)
clothing = Category("pants,shirt,dress", 1000)
carExpense = Category("Gas, service, repairs, car note", 200)

print(food.deposit())
print(clothing.deposit())
print(carExpense.deposit())


