class accout:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposite(self, amount):
        if amount <= 0:
            self._balance += amount
            print(f"[{self.owner}] received {amount}. current: {self._balance}")
        else:
