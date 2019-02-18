Nine is used instead of * for ease of checking. Otherwise the program should function identically to the instructions.
For example: python eightPuzzle.py <algorithm_name>
where algorithm_name can take one of the following values:
- bfs : For running the Breadth-first search algorithm
- ids : For running the Iterative deepening search algorithm
- astar1 : For running the A* algorithm with the Manhattan heuristic.
- astar2 : For running the A* algorithm with the difference heuristic.
(I'm not sure if there's a better name for the difference heuristic, but cost is the number of displaced numbers)
To test different starting values, you will have to change the start variable in the main function.

The Manhattan heuristic used in astar1 searches more nodes than the difference heuristic in astar2.
Therefore, for my test cases, the distance heuristic is more efficient than the Manhattan heuristic.

Raw Data (most test cases could not be solved by depth 10):
Manhattan, Difference
[9, 1, 3, 4, 2, 5, 7, 8, 6] - 33, 4
[1, 8, 2, 9, 4, 3, 7, 6, 5] - 440, 30