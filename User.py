# 1. Create a file with the User class, including the __init__ and make_deposit methods
class User: 

    def __init__( self, fN, lN ):
        # Attributes
        self.firstName = fN
        self.lastName = lN
        self.balance = 0
        # self.account = {
        #    "vacations" : BankAccount( 0.03, 500 ),
        #   "buyNewCar" : BankAccount( 0.03, 1500 )
        #}


# 3. Add a display_user_balance method to the User class
    def display_user_balance( self ):
        print(f"User: {self.firstName}  {self.lastName}, Balance: {self.balance}")

# BONUS: Add a transfer_money method (method's definition)
    def validateFunds(self, amount):
        if self.balance > amount:
            return True
        else:
            return False

    def transfer( self, user, amountToTransfer ):
        if self.validateFunds( amountToTransfer ):
            self.withdrawal( amountToTransfer )
            user.make_deposit( amountToTransfer )
        else:
            print( "You don't have enough funds to transfer." )

    

