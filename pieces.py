    
class chessPiece(): 
    def __init__(self, name, value, actualPosition):
        self.actualPosition = actualPosition
        self.value = value
        self.name = name
    def getName(self):
        return self.name
    
    def move(self, type):
        if (type is Pawn):
            pass
class Pawn(chessPiece):
    def __init__(self, name, value, actualPosition):
        super().__init__(name, value, actualPosition)
class Knight(chessPiece):
    def __init__(self, name, value, actualPosition):
        super().__init__(name, value, actualPosition)
class Bishop(chessPiece):
    def __init__(self, name, value, actualPosition):
        super().__init__(name, value, actualPosition)
class Rook(chessPiece):
    def __init__(self, name, value, actualPosition):
        super().__init__(name, value, actualPosition)
class Queen(chessPiece):
    def __init__(self, name, value, actualPosition):
        super().__init__(name, value, actualPosition)
class King(chessPiece):
    def __init__(self, name, value, actualPosition):
        super().__init__(name, value, actualPosition)