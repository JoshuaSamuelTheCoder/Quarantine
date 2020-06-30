class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        q = ["" for i in range(numRows)]
        i = 0
        inc = 1
        index = 0

        while index < len(s):
            q[i] += str(s[index])
            i += inc
            index += 1
            if i == numRows -1 or i == 0:
                inc *= -1

        st = ""
        for i in range(len(q)):
            st += q[i]


        return st
            
