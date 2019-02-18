from board2 import Board
class State:
    """ Handles the state of the game """

    def __init__(self, initialState=[]):
        self.current = Board(initialState)

    def __eq__(self, other):
        return self.current == other.current

    def __str__(self):
        return str(self.current)

    def __hash__(self):
        return hash(str(self))

    def up(self):
        up = self.current.up()
        if up:
            return State(up)
        else:
            return self

    def down(self):
        down = self.current.down()
        if down:
            return State(down)
        else:
            return self

    def left(self):
        left = self.current.left()
        if left:
            return State(left)
        else:
            return self

    def right(self):
        right = self.current.right()
        if right:
            return State(right)
        else:
            return self

    def successors(self):
        successors = []

        up = self.current.up()
        if up != None:
            successors.append(State(up))

        down = self.current.down()
        if down != None:
            successors.append(State(down))

        left = self.current.left()
        if left != None:
            successors.append(State(left))

        right = self.current.right()
        if right != None:
            successors.append(State(right))

        return successors
