class Board:

    def __init__(self):
        self.board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']]
        self.x = 0
        self.y = 0
        self.is_player_turn = True

    def PrintBoard(self):
        print("      |      |      ")
        print("  " + self.board[0][0] + "   |   " + self.board[0][1] + "  |   " + self.board[0][2] + "  ")
        print("      |      |      ")
        print("-----------------")
        print("      |      |      ")
        print("  " + self.board[1][0] + "   |   " + self.board[1][1] + "  |   " + self.board[1][2] + "  ")
        print("      |      |      ")
        print("-----------------")
        print("      |      |      ")
        print("  " + self.board[2][0] + "   |   " + self.board[2][1] + "  |   " + self.board[2][2] + "  ")
        print("      |      |      ")
        print()

    def FillSpace(self):
        if self.is_player_turn:
            self.board[self.x][self.y] = "X"
        else:
            self.board[self.x][self.y] = "O"

    def ConvertSpace(self, space):
        if space == 1:
            self.x = 0
            self.y = 0
        elif space == 2:
            self.x = 0
            self.y = 1
        elif space == 3:
            self.x = 0
            self.y = 2
        elif space == 4:
            self.x = 1
            self.y = 0
        elif space == 5:
            self.x = 1
            self.y = 1
        elif space == 6:
            self.x = 1
            self.y = 2
        elif space == 7:
            self.x = 2
            self.y = 0
        elif space == 8:
            self.x = 2
            self.y = 1
        elif space == 9:
            self.x = 2
            self.y = 2

    def CheckWin(self):
        # check if previous move caused a win on vertical line
        if self.board[0][self.y] == self.board[1][self.y] == self.board[2][self.y]:
            return True

        # check if previous move caused a win on horizontal line
        if self.board[self.x][0] == self.board[self.x][1] == self.board[self.x][2]:
            return True

        # check if previous move was on the main diagonal and caused a win
        if self.x == self.y and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True

        # check if previous move was on the secondary diagonal and caused a win
        if self.x + self.y == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True

        return False

    def isMovesLeft(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is not "O" and self.board[i][j] is not "X":
                    return True
        return False


# IF THE WINNER IS "O" THEN RETURN 10
def evaluate(b):
    for row in range(3):
        if b.board[row][0] == b.board[row][1] == b.board[row][2]:
            if b.board[row][0] == "O":
                return 5
            elif b.board[row][0] == "X":
                return -5
    for col in range(3):
        if b.board[0][col] == b.board[1][col] == b.board[2][col]:
            if b.board[0][col] == "O":
                return 5
            elif b.board[0][col] == "X":
                return -5
    if b.board[0][0] == b.board[1][1] == b.board[2][2]:
        if b.board[0][0] == "O":
            return 5
        elif b.board[0][0] == "X":
            return -5
    if b.board[0][2] == b.board[1][1] == b.board[2][0]:
        if b.board[0][2] == "O":
            return 5
        elif b.board[0][2] == "X":
            return -5
    return 0


def minimax(b, depth, isMax):
    score = evaluate(b)

    if score is 5:
        return score
    if score is -5:
        return score
    if not b.isMovesLeft():
        return 0

    if isMax:
        best = -1000

        for i in range(3):
            for j in range(3):
                if b.board[i][j] is not "O" and b.board[i][j] is not "X":
                    temp = b.board[i][j]
                    b.board[i][j] = "O"

                    best = max(best,
                               minimax(b, depth + 1, not isMax)) + depth
                    b.board[i][j] = temp
        return best
    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if b.board[i][j] is not "O" and b.board[i][j] is not "X":
                    temp = b.board[i][j]
                    b.board[i][j] = "X"

                    best = min(best,
                               minimax(b, depth + 1, not isMax)) - depth
                    b.board[i][j] = temp
        return best


def SuperiorRobotMove(b):
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):
            if b.board[i][j] is not "O" and b.board[i][j] is not "X":
                temp = b.board[i][j]
                b.board[i][j] = "O"

                moveVal = minimax(b, 0, False)

                b.board[i][j] = temp

                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    print(bestMove)
    return bestMove


def PlayGame(b):
    is_over = False
    while not is_over:
        if b.is_player_turn:
            space = int(input("Select a Space Bitch: "))
            b.ConvertSpace(space)
            if b.board[b.x][b.y] is not "X" and b.board[b.x][b.y] is not "O":
                b.FillSpace()
                b.is_player_turn = False
            else:
                print("That's not a Valid Space Idiot")
        else:
            move = SuperiorRobotMove(b)
            b.x = move[0]
            b.y = move[1]
            b.FillSpace()
            b.is_player_turn = True

        b.PrintBoard()
        if b.CheckWin():
            if b.is_player_turn:
                print("RoBoT Wins!")
            else:
                print("Player Wins!")
            is_over = True
        else:
            if not b.isMovesLeft():
                print("DRAW!")
                is_over = True


if __name__ == "__main__":
    gameBoard = Board()
    print("Welcome to Carmine's TicTacToe")
    gameBoard.PrintBoard()
    PlayGame(gameBoard)
