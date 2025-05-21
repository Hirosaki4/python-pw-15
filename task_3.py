class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Поповнення: +{amount} грн. Новий баланс: {self.balance} грн.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатньо коштів на рахунку!")
        else:
            self.balance -= amount
            print(f"Знято: -{amount} грн. Новий баланс: {self.balance} грн.")

    def check_balance(self):
        return f"Поточний баланс: {self.balance} грн."


# Приклад використання
account = BankAccount("Анна", "UA123456789", 1000)
print(account.check_balance())
account.deposit(500)
account.withdraw(2000)  # недостатньо коштів
account.withdraw(300)
print(account.check_balance())
