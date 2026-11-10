
class BankAccount:
    def __init__(self, amount):
        self.__balance = amount

    @property
    def balance(self):
        return self.__balance

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Money added successfully.")
        else:
            print("Please enter a positive amount.")

    def remove_money(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Money withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")


account = BankAccount(8000)

print("Initial Balance:", account.balance)

account.add_money(3000)
print("Updated Balance:", account.balance)

account.remove_money(2000)
print("Remaining Balance:", account.balance)
