class Category:

    def __init__(self, category, amount):
        self.amount = amount
        self.category = category


    #methods
    def deposit(self, amount):
        self.amount += amount
        return "{} was deposited in your {} account".format(amount, self.category)

    
        
    def check_balance(self):
        return "{} is the current balance in your {} account".format(self.amount, self.category)

    
    def withdrawl(self, amount):
        if self.check_balance():
            self.amount -= amount
            return "{} was withdrawn from your {} account".format(amount, self.category)
        else:
            return "Transaction fail..insufficient funds"
        

    def transfer(self, amount, category):
        if self.amount < amount:
            return "Transaction fail, Insufficient funds"
        
        else:
            self.amount -= amount
            category.amount += amount

            print("Transfer successful")


            return "{} was transfer from your {} account to your carExpense account to pay your car note".format(amount, self.category)


food = Category("food", 1000)
clothing = Category("clothing", 500)
carExpense = Category("carExpense", 200)
furniture = Category("furniture", 2000 )
Lodging = Category("Rent", 1000)

print(food.deposit(10))
print(food.withdrawl(20))
print(food.check_balance())

print(clothing.transfer(50, food))
print(clothing.deposit(5))
print(clothing.check_balance())

print(food.transfer(200, carExpense))
print(carExpense.withdrawl(30))
print(carExpense.check_balance(),)

print(furniture.deposit(50))
print(furniture.withdrawl(500))
print(furniture.check_balance())

print(Lodging.deposit(200))
print(Lodging.transfer(100,furniture))
print(Lodging.withdrawl(1500))
print(Lodging.check_balance())

print(food.check_balance())

