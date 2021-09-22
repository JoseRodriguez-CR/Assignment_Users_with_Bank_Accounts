class BankAccount:
    allBankAccounts = []

# Update the User class __init__ method
    def __init__(self, user, int_rate, balance): 
        self.user = user  #updated to received a object from main file
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.allBankAccounts.append( self )

#Update the User class make_deposit method
    def make_deposit( self, amount ):  # since user is not required here not changes were done
        self.balance += amount
        return self

#Update the User class make_withdrawal method
    def withdraw(self, amount):  # since user is not required here not changes were done
        if amount <= self.balance:
            self.balance -= amount
        else:
            print( "Insufficient funds: Charging a $5 fee" )
            self.balance -= 5
        return self

#Update the User class display_user_balance method
    def display_user_balance( self ):
        self.user.display_user_balance()  #updated to received a object from main file and sent it to class user
        return self

    def yield_interest( self, int_rate ):
        if(self.balance > 0):
            self.balance += self.balance * int_rate
            print(f"Your Balance Account has been increased by {int_rate},\nnow your Balance Accout has: ${self.balance}")
        return self   


    @classmethod
    def printAllAccountsInfo( cls ):
        for account in cls.allBankAccounts:
            account.display_user_balance()

            # print( f"Account number: {self.accountNum}." )


