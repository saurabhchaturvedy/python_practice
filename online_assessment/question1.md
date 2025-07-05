 Problem Statement:
You are given a 2D grid (matrix) representing values at different cells and a string moves representing a path of movement using the characters:

'U': move up,

'D': move down,

'L': move left,

'R': move right.

Starting from the top-left corner of the grid (position (0, 0)), you move according to the instructions in moves. Each move can expand the area that might be affected or "reachable" by some drop falling off the path.

Your task is to calculate the sum of all "safe" leaf values in the matrix — that is, cells which cannot be reached by extending the path in any of the four directions traced by the moves.

In simpler terms:

A cell is unsafe if it lies within the bounding box traced by the path (i.e., can be reached by extending from the initial position using the same movement pattern).

A cell is safe if it's outside that bounding box and hence unaffected by the movement.

Return the sum of all such "safe" cells.





matrix = [
    [1, 0, 2],
    [4, 1, 0],
    [0, 3, 1]
]
moves = "RR"
