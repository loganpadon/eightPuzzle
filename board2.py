class Board:
    """ The Board class represents the low-level physical configuration of the
        8-puzzle game. """

    # The 8-puzzle board can be represented as a list of length 8
    def __init__(self, initial_values=[]):
        self.value = initial_values

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(str(self))

    # If 0 is in the top most block, then up is invalid
    def up(self):
        pos = self.value.index(9)
        if pos in (0, 1, 2):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos-3] = new_val[pos-3], new_val[pos]
            return new_val

    # If 0 is in the bottom most block, then up is invalid
    def down(self):
        pos = self.value.index(9)
        if pos in (6, 7, 8):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos+3] = new_val[pos+3], new_val[pos]
            return new_val

    # If 0 is in the left most block, then up is invalid
    def left(self):
        pos = self.value.index(9)
        if pos in (0, 3, 6):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos-1] = new_val[pos-1], new_val[pos]
            return new_val

    # If 0 is in the right most block, then up is invalid
    def right(self):
        pos = self.value.index(9)
        if pos in (2, 5, 8):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos+1] = new_val[pos+1], new_val[pos]
            return new_val
