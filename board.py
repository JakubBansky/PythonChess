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
        for rows in board:
            for chessPiece in rows:
                print(chessPiece.name)
            print(rows)

    def initializeBoard(self, board):
        self.initEmptyBoard(board)
        for j in range(8):
            board[1][j] = pieces.Pawn([1, j])
            board[6][j] = pieces.Pawn([6, j])
        for k in range(0, 8, 7):
            board[0][k] = pieces.Rook
            board[7][k] = pieces.Rook
        for k in range(1, 7, 5):
            board[0][k] = pieces.Knight
            board[7][k] = pieces.Knight
        for k in range(2, 6, 3):
            board[0][k] = pieces.Bishop
            board[7][k] = pieces.Bishop
        for k in range(0, 8, 7):
            board[k][3] = pieces.Queen
        for k in range(0, 8, 7):
            board[k][4] = pieces.King


b = Board()
b.initializeBoard(b.board)
b.printBoard(b.board)
