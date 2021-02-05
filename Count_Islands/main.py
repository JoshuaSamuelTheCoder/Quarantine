"""
Given a 2D matrix, where 1 represents land and 0 represents water,
count how many islands are present

Input:
[
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0]
]

Island 1 = [(1, 0), (1, 1), (2, 0), (2, 2)]
Island 2 = [(2, 3), (2, 4), (3, 3)]
"""
from collections import deque

class Islands(object):

    def __init__(self):
        pass

    def isValid(self, position):
        x,y = position
        if x >= 0 and x < self.n and y >= 0 and y < self.m:
            return True
        return False

    def getNeighbors(self, position):
        x,y = position
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i,j) not in self.seen and self.isValid((i,j)):
                    if self.matrix[i][j] == 1:
                        self.seen.add((i,j))

    def bfs(self):
        count = 0

        while len(self.q) > 0:
            item = self.q.popleft()
            if item not in self.seen:
                count += 1
            neighbors = self.getNeighbors(item)
            
        return count

    def countIslands(self, matrix):
        #main method
        self.q = deque() #circular array with O(1) popleft() and popright()
        self.seen = set()
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.matrix = matrix

        for i in range(self.n):
            for j in range(self.m):
                if matrix[i][j] == 1:
                    self.q.append((i, j))

        return self.bfs()


if __name__ == "__main__":

    matrix = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 1, 0]]
    island = Islands()
    print(island.countIslands(matrix))
