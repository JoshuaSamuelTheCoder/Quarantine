"""
Given a chess board of n rows (top to bottom) and n columns (left to right),
In each, move a knight moves either:
    2 column positions and 1 row position
    2 row positions and 1 column position

In other words, a move is 2 steps along one axis and 1 step along a perpendicular axis.

Given a starting position A and ending position B, calculate the minimum number of moves needed by the knight
to move from A to B if it is possible else return -1.

Example:
n = 9
startRow = 4
starCol = 4
endRow = 4
endcol = 8

The chess board has a size of 9 x 9.
Starts at the position (startRow, startCol) = (4, 4)
Move 1 step up or down, then 2 steps right to reach either the position (3, 6) or (5, 6)
Move 2 steps right and 1 step down or up as necessary to reach the position (4,8)
The minimum number of moves to move from the position (4,4) to the position (4,8) is 2.

Input:
int n: the width and height of the square board
int startRow: the row of the starting location
int startCol: the column of the starting location
int endRow: the row of the target location
int endCol: the column of the target location

Output:
int: a single integer that denotes the number of moves required or -1 if it is not possible to reach the target location.

TestCase 0:
Input:
n = 10
startRow = 0
startCol = 0
endRow = 0
endCol = 2
Ouput:
2
Explanation:
The chessboard is of size 10 x 10. Start at the position (0,0). Move 2 steps down and 1 step right to reach the position (2,1).
Move 1 step right and 2 steps up to reach the position (0,2). The minimum number of moves to move from the position (0,0) to position (0,2) is 2.

TestCase 1:
Input:
n = 6
startRow = 5
startCol = 1
endRow = 0
endCol = 5
Output:
3
Explanation:
The chessboard is of size 6 x 6. Start at the position (5,1). Move 2 steps up and 1 right to position (3,2). Move 2 steps up and 1 right to position (1,3).
Move 1 step up and 2 steps right to reach the position (0,5), The minimum number of moves to move from the position (5,1) to position (0,5) is 3.
"""
from collections import deque
def Solution():

    def isValid(self, location):
        x,y = location
        if x >= 0 and x < self.length and y >=0 and y < self.length:
            return True
        return False

    def getNeighbors(self, location):
        x,y = location
        alongXAxis = [(x+1, y-2), (x+1, y+2), (x-1, y-2), (x-1, y+2)]
        alongYAxis = [(x-2, y+1), (x+2, y+2), (x-2, y-1), (x+2, y-1)]
        return alongXAxis + alongYAxis

    def bfs(self):

        job_lst = self.job_lst
        moves = 0
        while(len(job_lst) > 0):
            item, prior = job_lst.popleft()
            if item == self.goal:
                return prior
            neighbors = self.getNeighbors(item)
            for n in neighbors:
                if self.isValid(n) and n not in self.seen:
                    self.seen.add(n)
                    job_lst.append((n, prior+1))
        return -1

    def minMoves(self, n, startRow, startCol, endRow, endCol):
        self.seen = set()
        self.length = n

        self.start = (startRow, startCol)
        self.goal = (endRow, endCol)
        self.seen.add(self.start)
        self.job_lst = deque()
        self.job_lst.append((self.start, 0))

        return self.bfs()

def minMoves(n, startRow, startCol, endRow, endCol):
    sol = Solution()
    return sol.minMoves(n, startRow, startCol, endRow, endCol)
