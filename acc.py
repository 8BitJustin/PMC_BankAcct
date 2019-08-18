class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(str(amount) + " withdrawn.")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(str(amount) + " deposited.")

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


jack_checking = Checking("jack.txt", 1)
jack_checking.transfer(100)
print(jack_checking.balance)
jack_checking.commit()

john_checking = Checking("john.txt", 1)
john_checking.transfer(100)
print(john_checking.balance)
john_checking.commit()


# account = Account("balance.txt")

# Prints balance text of balance.txt file
# print(account.balance)

# Runs withdraw method
# account.withdraw(100)
# print(account.balance)

# Runs deposit method
# account.deposit(1000)
# print(account.balance)

# account.commit()

