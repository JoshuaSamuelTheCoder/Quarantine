"""
In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.



Note:

    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2.

"""
class Solution(object):

    def isValid(self, x, y):
        #determines whether coordinates are in the grid
        if y < 0 or y >= len(self.grid) or x < 0 or x >= len(self.grid[y]):
            return False
        return True

    def findValidNeighbors(self, coord):
        #gets neighbors that have been converted
        x,y = coord
        neighbors = []

        for i,j in [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]:
            if (i,j) not in self.seen and self.isValid(i,j) and self.grid[j][i] == 1:
                self.grid[j][i] = 2
                neighbors.append((i,j))
                self.num_fresh -= 1

        return neighbors

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        job_lst = []

        seen = set()

        self.seen = seen
        self.grid = grid

        self.num_fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    job_lst.append(((j,i), 0))
                elif grid[i][j] == 1:
                    self.num_fresh += 1

        counter = 0

        while len(job_lst) != 0:
            item, ts = job_lst.pop(0)

            neighbors = self.findValidNeighbors(item)

            if len(neighbors) > 0:
                counter = ts+1

            for n in neighbors:
                if n not in seen:
                    seen.add(n)
                    job_lst.append((n, ts+1))


        if self.num_fresh > 0:
            return -1

        return counter
