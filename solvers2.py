from collections import namedtuple
from queue import PriorityQueue
import itertools


def goalTest(state):
    return state.current.value == sorted(state.current.value)


def bfs(start):
    SearchPosition = namedtuple('SearchPos', 'node, depth, prev')
    position = SearchPosition(start, 0, None)

    frontier = [position]
    explored = set()

    while len(frontier) > 0:
        position = frontier.pop(0)
        currentNode = position.node

        try:
            if max([pos.depth for pos in frontier]) == 11:
                return None
        except ValueError:
            pass

        if goalTest(currentNode):
            Success = namedtuple('Success', 'position, nodesExpanded')
            success = Success(position, len(explored))
            return success

        explored.add(currentNode)

        for neighbor in currentNode.successors():
            newPosition = SearchPosition(neighbor, position.depth + 1, position)
            frontierCheck = neighbor in [pos.node for pos in frontier]
            if neighbor not in explored and not frontierCheck:
                frontier.append(newPosition)

    return None

def ids(start):
    for depth in range(1,10):
        route = dfs([start], depth)
        if route:
            return route, depth - 1

    return None

def dfs(route, depth):
    if depth == 0:
        return None

    if goalTest(route[-1]):
        return route

    for move in route[-1].successors():
        if move not in route:
            nextRoute = dfs(route + [move], depth-1)
            if nextRoute:
                return nextRoute

def astar1(start):
    counter = itertools.count()
    SearchPosition = namedtuple('SearchPos', 'node, depth, prev')
    position = SearchPosition(start, 0, None)

    currentNode = position.node
    frontier = PriorityQueue()
    frontier.put((manhattan(currentNode), next(counter), position))
    explored = list()

    while True:
        if frontier.empty():
            return None
        position = frontier.get()[2]
        currentNode = position.node
        if goalTest(currentNode):
            Success = namedtuple('Success', 'position, nodesExpanded')
            success = Success(position, len(explored))
            return success
        elif currentNode not in explored:
            explored.append(currentNode)
            successors = currentNode.successors()
            for child in successors:
                newPosition = SearchPosition(child, position.depth + 1, position)
                if(newPosition.depth <= 10):
                    frontier.put((manhattan(child)+newPosition.depth, next(counter), newPosition))

def astar2(start):
    counter = itertools.count()
    SearchPosition = namedtuple('SearchPos', 'node, depth, prev')
    position = SearchPosition(start, 0, None)

    currentNode = position.node
    frontier = PriorityQueue()
    frontier.put((difference(currentNode), next(counter), position))
    explored = list()
    while True:
        if frontier.empty():
            return None
        position = frontier.get()[2]
        currentNode = position.node
        if goalTest(currentNode):
            Success = namedtuple('Success', 'position, nodesExpanded')
            success = Success(position, len(explored))
            return success
        elif currentNode not in explored:
            explored.append(currentNode)
            successors = currentNode.successors()
            for child in successors:
                newPosition = SearchPosition(child, position.depth + 1, position)
                if(newPosition.depth <= 10):
                    frontier.put((difference(child)+newPosition.depth, next(counter), newPosition))


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
