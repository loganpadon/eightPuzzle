from collections import namedtuple
from queue import PriorityQueue
import itertools


def goal_test(state):
    return state.current.value == sorted(state.current.value)


# BFS Search
def bfs(start):
    """
    Performs breadth-first search starting with the 'start' as the beginning
    node. Returns a namedtuple 'Success' which contains namedtuple 'position'
    (includes: node, cost, depth, prev), 'max_depth' and 'nodes_expanded'
    if a node that passes the goal test has been found.

    """

    # SearchPos used for bookeeping and finding the path:
    SearchPos = namedtuple('SearchPos', 'node, cost, depth, prev')

    # Initial position does not have a predecessor
    position = SearchPos(start, 0, 0, None)


    # frontier contains unexpanded positions
    frontier = [position]
    explored = set()
    while len(frontier) > 0:

        # current position is the first position in the frontier
        position = frontier.pop(0)

        node = position.node

        try:
            if max([pos.depth for pos in frontier]) == 11:
                return None
        except ValueError:
            pass

        # goal test: return success if True
        if goal_test(node):
            max_depth = max([pos.depth for pos in frontier])
            Success = namedtuple('Success', 'position, max_depth, nodes_expanded')
            success = Success(position, max_depth, len(explored))
            return success

        # expanded nodes are added to explored set
        explored.add(node)

        # All reachable positions from current postion is added to frontier
        for neighbor in node.successors():
            new_position = SearchPos(neighbor, position.cost + 1, position.depth + 1, position)
            frontier_check = neighbor in [pos.node for pos in frontier]
            if neighbor not in explored and not frontier_check:
                frontier.append(new_position)

    # the goal could not be reached.
    return None

def ids(start):
    for depth in range(1,10):
        route = dfs([start], depth)
        if route:
            return route, depth

    return None

def dfs(route, depth):
    if depth == 0:
        return None

    if goal_test(route[-1]):
        return route

    for move in route[-1].successors():
        if move not in route:
            nextRoute = dfs(route + [move], depth-1)
            if nextRoute:
                return nextRoute

def astar1(start):
    counter = itertools.count()
    # SearchPos used for bookeeping and finding the path:
    SearchPos = namedtuple('SearchPos', 'node, cost, depth, prev')

    # Initial position does not have a predecessor
    position = SearchPos(start, 0, 0, None)

    actual = position.node
    leaves = PriorityQueue()
    leaves.put((manhattan(actual), next(counter), position))
    closed = list()
    while True:
        if leaves.empty():
            return None
        position = leaves.get()[2]
        actual = position.node
        if goal_test(actual):
            Success = namedtuple('Success', 'position, max_depth, nodes_expanded')
            success = Success(position, 0, 0)  # todo here
            return success
        elif actual not in closed:
            closed.append(actual)
            successors = actual.successors()
            for child in successors:
                new_position = SearchPos(child, position.cost + 1, position.depth + 1, position)
                #depth = max([pos.depth for pos in leaves])
                if(new_position.depth <= 10):
                    leaves.put((manhattan(child)+new_position.depth, next(counter), new_position)) #Figure out how to calculate depth

def astar2(start):
    counter = itertools.count()
    # SearchPos used for bookeeping and finding the path:
    SearchPos = namedtuple('SearchPos', 'node, cost, depth, prev')

    # Initial position does not have a predecessor
    position = SearchPos(start, 0, 0, None)

    actual = position.node
    leaves = PriorityQueue()
    leaves.put((difference(actual), next(counter), position))
    closed = list()
    while True:
        if leaves.empty():
            return None
        position = leaves.get()[2]
        actual = position.node
        if goal_test(actual):
            Success = namedtuple('Success', 'position, max_depth, nodes_expanded')
            success = Success(position, 0, 0) #todo here
            return success
        elif actual not in closed:
            closed.append(actual)
            successors = actual.successors()
            for child in successors:
                new_position = SearchPos(child, position.cost + 1, position.depth + 1, position)
                #depth = max([pos.depth for pos in leaves])
                if(new_position.depth <= 10):
                    leaves.put((difference(child)+new_position.depth, next(counter), new_position)) #Figure out how to calculate depth

def manhattan(state):
    value = state.current.value
    cube = [[value[0], value[1], value[2]],
            [value[3], value[4], value[5]],
            [value[6], value[7], value[8]]]
    h = 0
    for i in range(3):
        for j in range(3):
            x, y = divmod(cube[i][j], 3)
            h += abs(x-i) + abs(y-j)
    return h

def difference(state):
        value = state.current.value
        cube = [[value[0], value[1], value[2]],
            [value[3], value[4], value[5]],
            [value[6], value[7], value[8]]]
        goal = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
        h = 0
        for i in range(3):
            for j in range(3):
                if cube[i][j] != goal[i][j]:
                    h += 1
        return h
