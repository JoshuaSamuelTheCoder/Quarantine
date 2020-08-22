"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]


Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""

from collections import deque

class Solution(object):

    def isValid(self, x, y):
        if x < 0 or y < 0 or y >= len(self.matrix) or x >= len(self.matrix[y]):
            return False
        return True

    def dist(self, x1, y1, x2, y2):
        return abs(x2-x1) + abs(y2-y1)

    def getValidNeighbors(self, x, y):

        neighbors = []
        for i,j in [(x, y-1), (x, y+1), (x-1, y), (x+1,y)]:
            if self.isValid(i,j):
                neighbors.append((i,j))

        return neighbors

    def findClosestZero(self, location):
        x,y = location

        seen = set()

        neighbors = self.getValidNeighbors(x,y)
        minDist = float("inf")
        for i,j in neighbors:
            seen.add((i,j))
            if self.matrix[j][i] == 0:
                minDist = min(minDist, self.dist(x,y,i,j))
                self.matrix[y][x] = minDist
                break
            else:
                new_neighbors = self.getValidNeighbors(i,j)
                for n in new_neighbors:
                    if n not in seen:
                        neighbors.append(n)

        return minDist

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        self.matrix = matrix
        job_lst = deque()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    job_lst.append((j,i))

        #check all 1's
        while job_lst:
            self.findClosestZero(job_lst.popleft())

        return matrix
