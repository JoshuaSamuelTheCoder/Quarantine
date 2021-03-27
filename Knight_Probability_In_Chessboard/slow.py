from collections import deque
class Solution(object):
    def insideBoard(self, loc):
        r,c = loc
        if r < self.n and r >= 0 and c < self.n and c >= 0:
            return True
        return False

    def getNeighbors(self, loc):
        r,c = loc
        neighbors = [(r-2, c-1), (r-2, c+1), (r-1, c-2), (r-1, c+2), (r+1, c-2), (r+1, c+2), (r+2, c-1), (r+2, c+1)]
        #for i,j in [(r-2, c-1), (r-2, c+1), (r-1, c-2), (r-1, c+2), (r+1, c-2), (r+1, c+2), (r+2, c-1), (r+2, c+1)]:
        #    neighbors.append((i,j))
            #if (i,j) not in self.seen:
            #    neighbors.append((i,j))
            #    self.seen.add((i,j))
        return neighbors

    def dfs(self):
        while len(self.moves) > 0:
            item, val, multiplier = self.moves.pop()
            if val == self.k:
                self.probability += multiplier
                continue
            neighbors = self.getNeighbors(item)
            inside = 0.0

            length = 0.0 + len(neighbors)
            x,y = item
            for i,j in self.valid_paths:
                n = (x+i, y+j)

                if self.insideBoard(n):
                    inside += 1

                    self.moves.append((n,val+1, multiplier/length))
            if len(self.moves) == 0:
                self.probability += (inside/length)*multiplier

            #self.probability += (inside/total)*multiplier

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

        self.memo = {}
        self.probability = 0.0
        self.multiplier = 1.0

        self.valid_paths = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        self.moves = deque()
        self.moves.append(((r,c), 0, 1))
        self.seen = {}
        self.dfs()
        return self.probability
