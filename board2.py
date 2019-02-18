class Board:
    """ The Board class represents the low-level physical configuration of the
        8-puzzle game. """

    # The 8-puzzle board can be represented as a list of length 8
    def __init__(self, initialValues=[]):
        self.value = initialValues

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(str(self))

    # If 0 is in the top most block, then up is invalid
    def up(self):
        position = self.value.index(9)
        if position in (0, 1, 2):
            return None
        else:
            newBoard = list(self.value)
            newBoard[position], newBoard[position-3] = newBoard[position-3], newBoard[position]
            return newBoard

    # If 0 is in the bottom most block, then up is invalid
    def down(self):
        position = self.value.index(9)
        if position in (6, 7, 8):
            return None
        else:
            newBoard = list(self.value)
            newBoard[position], newBoard[position+3] = newBoard[position+3], newBoard[position]
            return newBoard

    # If 0 is in the left most block, then up is invalid
    def left(self):
        position = self.value.index(9)
        if position in (0, 3, 6):
            return None
        else:
            newBoard = list(self.value)
            newBoard[position], newBoard[position-1] = newBoard[position-1], newBoard[position]
            return newBoard

    # If 0 is in the right most block, then up is invalid
    def right(self):
        position = self.value.index(9)
        if position in (2, 5, 8):
            return None
        else:
            newBoard = list(self.value)
            newBoard[position], newBoard[position+1] = newBoard[position+1], newBoard[position]
            return newBoard
