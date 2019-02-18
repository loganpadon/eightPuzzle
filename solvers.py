from collections import deque, namedtuple
from board import Board
def bfs(startingBoard):
    SearchPosition = namedtuple('SearchPosition', 'board, cost, depth, prev')

    position = SearchPosition(startingBoard, 0, 0, None)
    frontier = deque([position])
    print(frontier)
    #frontierSet = {position}
    explored = set()
    while frontier:
        position = frontier.popleft()
        board = position.board
        if board.goalCheck:
            maxDepth = max([position.depth for position in frontier])
            Success = namedtuple('Success', 'position, maxDepth, nodesExpanded')
            success = Success(position, maxDepth, len(explored))
            return success

        explored.add(board)
        for neighbor in board.validSuccessors():
            newPosition = SearchPosition(neighbor, position.cost+1, position.depth+1, position)
            frontierCheck = neighbor in [position.board for position in frontier]
            if neighbor not in explored and not frontierCheck:
                frontier.append(newPosition)

    return None
