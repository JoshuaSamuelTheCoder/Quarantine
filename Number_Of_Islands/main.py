"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



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
class Solution(object):

    def isValid(self,x,y):

        if x < 0 or x >= len(self.grid[0]) or y < 0 or y >= len(self.grid ):
            return False
        return True

    def search(self, x, y):

        if self.isValid(x,y):
            if (x,y) not in self.seen:
                if self.grid[y][x] == "1" and (x,y) not in self.seen:
                    self.seen.add((x,y))
                    for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                        self.search(i,j)


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        self.grid = grid
        self.num_islands = 0
        self.seen = set()

        for j in range(len(self.grid)):
            for i in range(len(self.grid[j])):
                if self.grid[j][i] == "1" and (i,j) not in self.seen:
                    self.search(i,j)
                    self.num_islands += 1

        return self.num_islands
