class Category:

    def __init__(self, category, amount):
       # self.food = food
        self.category = category
       # self.carExpense = carExpense
        self.amount = amount

    #methods
    def deposit(self, amount):
        self.amount += amount
        return "{} was deposited in your {} account for bread and milk".format(amount, self.category)

    def budget_balance(self):
        return "your available balance is {} in your account".format(self.amount)
    
        
    def check_balance(self, amount):
        self.amount <= amount
        return "{} is the current balance in your {} account".format(amount, self.category)

   # def budget_balance(self):
        #return "your available balance is {} for food".format(self.amount)
    

    

    def withdrawl(self, amount):
        self.amount -= amount
        return "{} was withdrawn from your {} account to pay your phone bill".format(amount, self.category)

    
        

    def transfer(self, amount):
        self.amount - amount
        return "{} was transfer from your {} account to your carExpense account to pay your car note".format(amount, self.category)



food = Category("Food", 1000)
clothing = Category("clothing", 500)
carExpense = Category("carExpense", 200)


print(food.deposit(10))
print(food.budget_balance())

print(clothing.check_balance(500))
print(clothing.budget_balance())



print(food.withdrawl(100))
print(food.budget_balance())

print(food.transfer(200))
print(carExpense.check_balance(200))
print(carExpense.budget_balance())
print(clothing.budget_balance())



