from collections import deque
class Solution(object):

    def getValidNeighbors(self, loc):

        x,y = loc
        neighbors = []
        for a in range(x-1, x+2):
            for b in range(y-1, y+2):
                if (a,b) not in self.seen:
                    self.seen.add((a,b))
                    if a == x and b == y:
                        pass
                    else:
                        neighbors.append((a,b))
        return neighbors

    def findOptimalPath(self, start, end):

        job_lst = deque()
        job_lst.append((start, 0))

        self.seen = set()
        self.seen.add(start)

        while(len(job_lst) > 0):
            loc, val = job_lst.popleft()

            neighbors = self.getValidNeighbors(loc)

            for n in neighbors:
                if n != end:
                    job_lst.append((n, val + 1))
                else:
                    return val + 1


    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cost = 0
        start = points[0]
        for i in range(1, len(points)):
            p = points[i]
            cost += self.findOptimalPath((start[0], start[1]), (p[0], p[1]))
            start = p

        return cost
