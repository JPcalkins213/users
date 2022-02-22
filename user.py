class User:
    bank_name = 'First national Dojo'
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.name) 
        print(self.account_balance)
        return self
    def transfer_money(self, other_user, ammount):
        self.account_balance -= ammount
        ammount += other_user
        other_user = self.account_balance
        return self


guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawl(25).display_user_balance()

#just ignore this comment
