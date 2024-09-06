class Wallet:
    #instance variables
    #constructor
    def __init__(self,colour,shape,pockets):
        self.colour=colour
        self.shape=shape
        self.pockets=pockets
    def describe(self):
        print(f"This wallet is {self.colour} coloured and has {self.pockets} pockets. ")
#creating objects
wallet1=Wallet("brown","square",5)
print(wallet1.colour)
wallet1.describe()
wallet2=Wallet("black","rectangle",18)
print(wallet2.colour)
wallet2.describe()