from state2 import State
import solvers2
from sys import argv


def main():
    start = [9, 1, 3, 4, 2, 5, 7, 8, 6]
    game = State(start)
    result = None
    depth = 0

    if argv[1] == 'bfs':
        result = solvers2.bfs(game)
    elif argv[1] == 'ids':
        result, depth = solvers2.ids(game)
    elif argv[1] == 'astar1':
        result = solvers2.astar1(game)
    elif argv[1] == 'astar2':
        result = solvers2.astar2(game)

    if not result:
        print("No result found in time")
    elif argv[1] == 'ids':
        print("Move sequence")
        tracePathD(result)
        print("Search depth:")
        print(depth)
    else:
        finalPosition = result.position
        nodesExpanded = result.nodesExpanded

        print("Move sequence:", tracePath(finalPosition))
        print("Nodes expanded:", nodesExpanded)
        print("Number of steps:", finalPosition.depth)


if __name__ == '__main__':
    main()


def tracePath(lastPosition):
    position = lastPosition.prev
    nextPosition = lastPosition

    path = []

    while position != None:
        if position.node.up() == nextPosition.node:
            path.append("Up")
        elif position.node.down() == nextPosition.node:
            path.append("Down")
        elif position.node.left() == nextPosition.node:
            path.append("Left")
        elif position.node.right() == nextPosition.node:
            path.append("Right")

        position = position.prev
        nextPosition = nextPosition.prev

    return path[::-1]


def tracePathD(route):
    for state in route:
        print(state.current.value)
