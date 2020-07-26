class Solution(object):

    def isValid(self, x,y):

        if x < 0 or x >= len(self.grid[0]) or y < 0 or y >= len(self.grid):
            return False
        return True

    def getNeighbors(self, x,y):

        neighbors = []
        #exclude x,y case
        for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if (i,j) not in self.seen and self.isValid(i,j):

                    if self.grid[j][i] == "1":
                        neighbors.append((i,j))
        return neighbors


    def search(self, x, y):

        job_lst = []
        if self.grid[y][x] == "1":
            self.num_islands += 1
            job_lst.append((x,y))
        else:
            self.seen.append((x,y))



        while job_lst:
            i,j = job_lst.pop(0)

            if (i,j) not in self.seen:
                self.seen.append((i,j))
                neighbors = self.getNeighbors(i,j)
                for n in neighbors:
                    job_lst.append(n)



    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if len(grid) == 0:
            return 0

        self.grid = grid
        self.seen = []
        self.num_islands = 0

        len_to_terminate = len(grid)*len(grid[0])

        i = 0
        j = 0

        while len(self.seen) < len_to_terminate:
            if i == len(grid[0]):
                j += 1
                i = 0
            if (i,j) not in self.seen:
                self.search(i,j)
            i += 1
        return self.num_islands
