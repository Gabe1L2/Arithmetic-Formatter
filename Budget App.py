class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        output = ""

        # title line
        num_of_asteriks = (30 - len(self.category)) // 2
        output += "*" * num_of_asteriks + self.category + "*" * num_of_asteriks + "\n"

        # prints all transactions
        for transaction in self.ledger:
            short_desc = transaction["description"][:23] # gets only up to 23 characters of the description
            amount = transaction["amount"]
            string_amount = f"{amount:.2f}" # forces the two decimal spots
            number_of_spaces = 30 - len(short_desc) # gets the room left for amount + spaces
            number_of_spaces -= len(string_amount) # minus the room used by the amount
            # transaction line
            output += short_desc + " " * number_of_spaces + string_amount + "\n"

        # print total
        total = self.get_balance()
        output += f"Total: {total}"

        return output

    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description
            })

    def withdraw(self, amount, description=""):
        # check if there's enough money
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            'amount': -amount,
            'description': description
            })
        
        return True

    def get_balance(self): # get ledger balance
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]

        return balance

    def transfer(self, amount, transfer_category):
        # check if there's enough money
        if not self.check_funds(amount):
            return False
        
        description = f"Transfer to {transfer_category.category}"
        self.withdraw(amount, description)

        description2 = f"Transfer from {self.category}"
        transfer_category.deposit(amount, description2)

        return True

    def check_funds(self, amount): # Gets ledger balance and sees if the amount is greater than the balance
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True
        
    def category_withdraws(self):
        withdraw_total = 0
        for transaction in self.ledger:
            if transaction["amount"] < 0:
                withdraw_total -= transaction["amount"]

        return withdraw_total
    
    def category_withdraw_percent(self, categories):
        total_withdraw = 0
        # get total spent on withdraws
        for cat in categories:
            total_withdraw += cat.category_withdraws()

        category_percent = self.category_withdraws() / total_withdraw
        percent_fix = (category_percent // .1) * .1
        return percent_fix
    

# bar chart
def create_spend_chart(categories):
    category_percents = []
    for cat in categories:
        category_percents.append(cat.category_withdraw_percent(categories))

    bar_chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        number_space = 3 - len(str(i))
        bar_chart += " " * number_space + str(i) + "| "
        for j, cat in enumerate(categories):
            if category_percents[j] * 100 >= i:
                bar_chart += "o  "
            else:
                bar_chart += "   "
        bar_chart += "\n"
    
    bar_chart += "    -" + "---" * len(categories)

    # get longest category name
    max_name_length = 0
    for cat in categories:
        if len(cat.category) > max_name_length:
            max_name_length = len(cat.category)

    for i in range(max_name_length):
        bar_chart += "\n"
        bar_chart += "     "
        for cat in categories:
            try:
                bar_chart += cat.category[i] + "  "
            except IndexError:
                bar_chart += "   "





    





    return bar_chart



food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25.45)
print(food)

print(create_spend_chart([food, clothing]))