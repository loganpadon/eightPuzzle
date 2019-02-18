# from board import Board
# import solvers
#
#
# def main():
#     board = ['*', 1 , 3 , 4, 2, 5, 7, 8, 6]
#     board = Board(board)
#     print(solvers.bfs(board))
#
#
# if __name__ == '__main__':
#     main()
from state2 import State
import solvers2
import time
# import resource


def trace_path(last_pos):
    pos = last_pos.prev
    next_pos = last_pos

    path = []

    while pos != None:
        if pos.node.up() == next_pos.node:
            path.append("Up")
        elif pos.node.down() == next_pos.node:
            path.append("Down")
        elif pos.node.left() == next_pos.node:
            path.append("Left")
        elif pos.node.right() == next_pos.node:
            path.append("Right")

        pos = pos.prev
        next_pos = next_pos.prev

    return path[::-1]

def trace_pathD(route):
    for state in route:
        print(state.current.value)


start_time = time.time()
config = [9, 1, 3, 4, 2, 5, 7, 8, 6]

game = State(config)

result = solvers2.bfs(game)
if result == None:
    print("No value found in time")
else:
    final_pos = result.position
    max_depth = result.max_depth
    nodes_expanded = result.nodes_expanded

    print("path_to_goal:", trace_path(final_pos))
    print("cost_of_path:", final_pos.cost)
    print("nodes_expanded:", nodes_expanded)
    print("search_depth:", final_pos.depth)
    print("max_search_depth:", max_depth)
    print("running_time:", time.time() - start_time)

result, depth = solvers2.ids(game)
trace_pathD(result)
print(depth)

result = solvers2.astar1(game)
final_pos = result.position
print(trace_path(final_pos))

result = solvers2.astar2(game)
final_pos = result.position
print(trace_path(final_pos))

start_time = time.time()
config = [1, 4, 3, 5, 2, 9, 7, 8, 6]

game = State(config)

result = solvers2.bfs(game)
if result == None:
    print("No value found in time")
else:
    final_pos = result.position
    max_depth = result.max_depth
    nodes_expanded = result.nodes_expanded

    print("path_to_goal:", trace_path(final_pos))
    print("cost_of_path:", final_pos.cost)
    print("nodes_expanded:", nodes_expanded)
    print("search_depth:", final_pos.depth)
    print("max_search_depth:", max_depth)
    print("running_time:", time.time() - start_time)