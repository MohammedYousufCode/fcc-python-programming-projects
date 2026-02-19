

class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]

    def deposit(self,amount,description=""):
        self.ledger.append({'amount':amount,'description':description})
    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount,'description':description})
            return True
        else:
            return False

    def get_balance(self):
        total=sum(item['amount'] for item in self.ledger)
        return total
    def transfer(self,amount,destination):
        if self.withdraw(amount,f'Transfer to {destination.name}'):
            destination.deposit(amount,f"Transfer from {self.name}")
            return True
        else:
            return False
    def check_funds(self,amount):
        if self.get_balance()>=amount:
            return True
        else:
            return False
    def __str__(self):
        title=self.name.center(30,'*')
        entries=""
        for item in self.ledger:
            desc=item['description'][:23]
            amt=f"{item['amount']:.2f}"
            entries+=f"{desc:<23}{amt:>7}\n"
        total=f"Total: {self.get_balance():.2f}"
        return title+"\n"+entries+total
import math

def create_spend_chart(categories):
    title = "Percentage spent by category"
    total_wit = 0
    withdrawals = []

    # Step 1: collect withdrawals
    for category in categories:
        cat_wit = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        withdrawals.append(cat_wit)
        total_wit += cat_wit

    # Step 2: convert to percentages (rounded down to nearest 10)
    percentages = [
        math.floor((wit / total_wit) * 100 / 10) * 10
        for wit in withdrawals
    ]

    # Step 3: build chart lines (100 → 0)
    chart = title + "\n"
    for level in range(100, -1, -10):
        chart += str(level).rjust(3) + "|"
        for p in percentages:
            chart += " o " if p >= level else "   "
        chart += " \n"

    # Step 4: horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Step 5: category names vertically
    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        chart += "     "
        for c in categories:
            chart += (c.name[i] + "  ") if i < len(c.name) else "   "
        chart += "\n"

    return chart.rstrip("\n")  # remove trailing newline
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(200, "groceries")
clothing.deposit(500, "initial deposit")
clothing.withdraw(50, "shirt")
auto.deposit(1000, "initial deposit")
auto.withdraw(300, "fuel")
print(create_spend_chart([food, clothing, auto]))
print(food,"\n",clothing,"\n",auto)


