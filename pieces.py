    
class chessPiece(): 
    def __init__(self, color):
        self.color = color
        self.actualPosition = []
        self.value = 0
    def move(self, type):
        if (type is Pawn):
            pass
class Pawn(chessPiece):
    def __init__(self, actualPosition):
        self.value = 1
        self.actualPosition = actualPosition
class Knight(chessPiece):
    def __init__(self):
        self.value = 3
class Bishop(chessPiece):
    def __init__(self):
        self.value = 3
class Rook(chessPiece):
    def __init__(self):
        self.value = 5
class Queen(chessPiece):
    def __init__(self):
        self.value = 10
class King(chessPiece):
    def __init__(self):
        self.value = 100