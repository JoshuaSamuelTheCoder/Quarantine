"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.


Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
"""

from collections import deque
class Solution(object):
    def insideBoard(self, loc):
        r,c = loc
        if r < self.n and r >= 0 and c < self.n and c >= 0:
            return True
        return False

    def dfs(self, start, prob, k):

        x,y = start
        p = 0.0
        if self.insideBoard(start):
            if k < self.k:
                for i,j in self.valid_paths:
                    dx,dy = x+i, y+j
                    if((dx,dy,k+1)) not in self.seen:
                        self.seen[(dx,dy,k+1)] = self.dfs((dx,dy), prob/8.0, k+1)
                    p += self.seen[(dx,dy,k+1)]
            else:
                return prob
        return p

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """

        #r,c -> 8 different locations, 8 times.
        #if within_board at the end, increment counter
        #return counter/total possibilities

        self.n = N
        self.k = K

        self.valid_paths = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        self.seen = {}
        p = self.dfs((r,c), 1.0, 0)
        return p
