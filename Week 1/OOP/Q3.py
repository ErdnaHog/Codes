# things i need
# - account number
# - account balance
# - interest rate


class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__account_balance, self.__interest_rate = self.make_bank_account(account_number)

    def make_bank_account(self, account_number):
        if account_number[0] == "1":
            return 500, 0.01
        else:
            return 500, 0.005

    def get_account_number(self):
        return print(f"Your account number is {self.__account_number}")

    def get_account_balance(self):
        return print(f"You have {self.__account_balance}")

    def get_interest_rate(self):
        return print(f"Your interest rate is {self.__interest_rate}")

    def get_interest(self):
        return print(f"Your interest earned is {self.__interest_rate * self.__account_balance}")

    def deposit_amount(self, deposit_amount):
        self.__account_balance += deposit_amount

    def withdraw_amount(self,withdraw_amount):
        if self.__account_balance < withdraw_amount:
            print("You have insufficient amount to withdraw")
        else:
            self.__account_balance -= withdraw_amount
            print(f"You are left with {self.__account_balance}")


account_balance = input("Enter account number: ")
bankAccount = BankAccount(account_balance)

option = "1"
while option != "0":
    option = input('''
1: Show account number
2: Show account balance
3: Show interest rate
4: Show interest earned
5: Deposit amount
6: Withdraw amount - 100
7: Withdraw amount - manually set
0: Exit
Option: ''')
    print()
    if option == "1":
        bankAccount.get_account_number()
    elif option == "2":
        bankAccount.get_account_balance()
    elif option == "3":
        bankAccount.get_interest_rate()
    elif option == "4":
        bankAccount.get_interest()
    elif option == "5":
        deposit_amount = int(input("Enter deposit amount"))
        bankAccount.deposit_amount(deposit_amount)
    elif option == "6":
        bankAccount.withdraw_amount(100)
    elif option == "7":
        withdraw_amount = int(input("What is the amount you want to withdraw?"))
        bankAccount.withdraw_amount(withdraw_amount)
