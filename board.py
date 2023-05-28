import pieces


class Board():
    def __init__(self):
        self.board = []

    def initEmptyBoard(self, board):
        for i in range(8):
            row = []
            for j in range(8):
                row.append(0)
            board.append(row)
    def printBoard(self, board):
        for row in board:
            for chessPiece in row:
                if chessPiece != 0:
                    print(chessPiece.name, end=" ")
                else:
                    print("0", end=" ")
            print()

    def initializeBoard(self, board):
        self.initEmptyBoard(board)
        for j in range(8):
            board[1][j] = pieces.Pawn("p", 1,[1, j])
            board[6][j] = pieces.Pawn("p", 1,[6, j])
        for k in range(0, 8, 7):
            board[0][k] = pieces.Rook("r", 5 , [0, k])
            board[7][k] = pieces.Rook("r", 5 , [7, k])
        for k in range(1, 7, 5):
            board[0][k] = pieces.Knight("k", 3 , [0, k])
            board[7][k] = pieces.Knight("k", 3 , [7, k])
        for k in range(2, 6, 3):
            board[0][k] = pieces.Bishop("b", 3 , [0, k])
            board[7][k] = pieces.Bishop("b", 3 , [7, k])
        for k in range(0, 8, 7):
            board[k][3] = pieces.Queen("q", 10 , [k, 3])
        for k in range(0, 8, 7):
            board[k][4] = pieces.King("K", 100 , [k, 4])


b = Board()
b.initializeBoard(b.board)
b.printBoard(b.board)
