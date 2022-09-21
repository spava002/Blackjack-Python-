class Player:
    def __init__(self, name, balance = 5):
        self.name = name
        self.balance = balance

    def getName(self):
        return self.name

    def getBalance(self):
        return self.balance

    def setBet(self):
        self.bet = int(input("Let us start with a bet. Please input an amount: $"))
        if self.bet <= 0:
            print(f"A bet of ${self.bet} can't be set!")
        if self.bet <= self.balance:
            self.balance = self.balance - self.bet
            print(f"A bet of ${self.bet} has been set. Remaining balance: ${self.balance}")
        else:
            print(f"A bet of ${self.bet} exceeds your current balance of: ${self.balance}. Try again.")
            Player.setBet(self)

    def winBalance(self):
        self.balance = self.balance + (self.bet * 2)
        print(f"Your new balance is: ${self.balance}")

    def lossBalance(self):
        newBalance = self.balance
        self.balance = newBalance
        print(f"Your new balance is: ${self.balance}")

    def tieBalance(self):
        self.balance = self.balance + self.bet
        print(f"Your new balance is: ${self.balance}")