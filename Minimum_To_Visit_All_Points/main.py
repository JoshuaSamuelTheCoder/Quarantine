class Solution(object):

    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cost = 0
        s = points[0]
        for i in range(1, len(points)):
            p = points[i]
            cost += max(abs(p[1]-s[1]), abs(p[0]-s[0]))
            s = p

        return cost
