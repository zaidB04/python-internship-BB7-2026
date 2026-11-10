class Account:
    def get_interest_rate(self):
        return 6


class SavingsAccount(Account):
    def get_interest_rate(self):
        return 8


class FixedDeposit(Account):
    def get_interest_rate(self):
        return 9


accounts = [
    Account(),
    SavingsAccount(),
    FixedDeposit()
]

for account in accounts:
    print("Interest Rate:", account.get_interest_rate(), "%")