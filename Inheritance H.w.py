class Boardgame:
    def __init__(self,dice,size,portable):
        self.dice=dice
        self.size=size
        self.portable=portable
    def details(self):
        print(f"size: {self.size}")
game1=Boardgame("yes","small","yes")
game1.details()

class Ludo(Boardgame):
    def __init__(self,dice,size,portable,players):
        Boardgame.__init__(self,dice,size,portable)
        self.players=players
    def player(self):
        print(f"palyers: {self.players}")
    def det_ludo(self):
        print(f"size: {self.size} palyers: {self.players} portable={self.portable} dice={self.dice}")
game2=Ludo("yes","small","yes","4")
game2.player()
game2.det_ludo()