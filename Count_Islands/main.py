"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
#isValid -> check if a node is within the matrix
#getNeighbors -> get neighbors from a given node
#dfs -> run dfs on a given node
#numberOfIslands -> iterate through matrix, append numbers to a list

from collections import deque

class Solution(object):

    def isValid(self, loc):
        x, y  = loc
        if x >= 0 and x < len(self.grid) and y >= 0 and y < len(self.grid[x]):
            return True
        return False

    def getValidNeighbors(self, loc):
        x, y = loc
        neighbors = []
        for dx,dy in self.paths:
            new_x = x + dx
            new_y = y + dy
            node = (new_x, new_y)
            if self.isValid(node) and node not in self.seen:
                neighbors.append(node)
        return neighbors


    def dfs(self):

        while len(self.job_lst) > 0:
            item = self.job_lst.pop() #O(1)

            neighbors = self.getValidNeighbors(item)

            for n in neighbors:
                i,j = n
                if self.grid[i][j] == "1":
                    self.seen.add(n)
                    self.job_lst.append(n)
        self.count += 1


    def numIslands(self, grid):

        self.grid = grid
        self.seen = set()
        self.job_lst = []
        self.count = 0
        #self.paths = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
        self.paths = [(-1,0), (0,-1), (0,1), (1,0)]


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                node = (i,j)
                if node not in self.seen and grid[i][j] == "1":
                    self.seen.add(node)
                    self.job_lst.append((i,j))
                    self.dfs()

        return self.count
