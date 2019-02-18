from state2 import State
import solvers2
from sys import argv

# def main():
#     start = [9, 1, 3, 4, 2, 5, 7, 8, 6]
#     game = State(start)
#     result = None
#     depth = 0
#
#     if argv[1] == 'bfs':
#         result = solvers2.bfs(game)
#     elif argv[1] == 'ids':
#         result, depth = solvers2.ids(game)
#     elif argv[1] == 'astar1':
#         result = solvers2.astar1(game)
#     elif argv[1] == 'astar2':
#         result = solvers2.astar2(game)
#
#     if not result:
#         print("No result found in time")
#     elif argv[1] == 'ids':
#         print("Move sequence")
#         trace_pathD(result)
#         print("Search depth:")
#         print(depth)
#     else:
#         finalPosition = result.position
#         nodesExpanded = result.nodes_expanded
#
#         print("Move sequence:", trace_path(finalPosition))
#         print("Nodes expanded:", nodesExpanded)
#         print("Number of steps:", finalPosition.depth)
#
#
# if __name__ == '__main__':
#     main()


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

config = [8, 1, 3, 4, 9, 2, 7, 6, 5]

game = State(config)

result = solvers2.bfs(game)
if result == None:
    print("No value found in time")
else:
    final_pos = result.position
    nodes_expanded = result.nodes_expanded

    print("path_to_goal:", trace_path(final_pos))
    print("nodes_expanded:", nodes_expanded)
    print("search_depth:", final_pos.depth)
    print("")

# result, depth = solvers2.ids(game)
# trace_pathD(result)
# print(depth)

result = solvers2.astar1(game)
if result == None:
    print("No value found in time")
else:
    final_pos = result.position
    nodes_expanded = result.nodes_expanded

    print("path_to_goal:", trace_path(final_pos))
    print("nodes_expanded:", nodes_expanded)
    print("search_depth:", final_pos.depth)
    print("")


result = solvers2.astar2(game)
if result == None:
    print("No value found in time")
else:
    final_pos = result.position
    nodes_expanded = result.nodes_expanded

    print("path_to_goal:", trace_path(final_pos))
    print("nodes_expanded:", nodes_expanded)
    print("search_depth:", final_pos.depth)
    print("")

config = [1, 4, 3, 5, 2, 9, 7, 8, 6]

game = State(config)

result = solvers2.bfs(game)
if result == None:
    print("No value found in time")
else:
    final_pos = result.position
    nodes_expanded = result.nodes_expanded

    print("path_to_goal:", trace_path(final_pos))
    print("nodes_expanded:", nodes_expanded)
    print("search_depth:", final_pos.depth)
    print("")

result = solvers2.astar1(game)
if result == None:
    print("No value found in time")
else:
    final_pos = result.position
    nodes_expanded = result.nodes_expanded

    print("path_to_goal:", trace_path(final_pos))
    print("nodes_expanded:", nodes_expanded)
    print("search_depth:", final_pos.depth)
    print("")

result = solvers2.astar2(game)
if result == None:
    print("No value found in time")
else:
    final_pos = result.position
    nodes_expanded = result.nodes_expanded

    print("path_to_goal:", trace_path(final_pos))
    print("nodes_expanded:", nodes_expanded)
    print("search_depth:", final_pos.depth)
    print("")
