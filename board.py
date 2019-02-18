class Board:
    def __init__(self, startingBoard):
        self.startingBoard = startingBoard

    def __str__(self):
        return str(self.startingBoard)

    def up(self):
        position = self.startingBoard.index('*')
        if position == 6 or position == 7 or position == 8:
            raise IllegalMove
        else:
            newState = list(self.startingBoard)
            newState[position], newState[position+3] = newState[position+3], newState[position]
            return Board(newState)

    def down(self):
        position = self.startingBoard.index('*')
        if position == 6 or position == 7 or position == 8:
            raise IllegalMove
        else:
            newState = list(self.startingBoard)
            newState[position], newState[position-3] = newState[position-3], newState[position]
            return newState

    def right(self):
        position = self.startingBoard.index('*')
        if position == 2 or position == 5 or position == 8:
            raise IllegalMove
        else:
            newState = list(self.startingBoard)
            newState[position], newState[position+1] = newState[position+1], newState[position]
            return newState

    def left(self):
        position = self.startingBoard.index('*')
        if position == 0 or position == 3 or position == 6:
            raise IllegalMove
        else:
            newState = list(self.startingBoard)
            newState[position], newState[position-1] = newState[position-1], newState[position]
            return newState

    def validSuccessors(self):
        moves = self.up, self.down, self.right, self.left
        for move in moves:
            try:
                yield move()
            except IllegalMove:
                pass

    def goalCheck(self):
        return self.startingBoard == sorted(self.startingBoard)

class IllegalMove(Exception):
    """Raised when an illegal move happens on the board"""
    pass
