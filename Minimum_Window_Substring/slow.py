import heapq
import sys

sys.setrecursionlimit(20000000)

class Solution(object):
    def contains(self, st_original):
        st = st_original
        if len(st) < len(self.T):
            return False

        for i in range(len(self.T)):
            if self.T[i] not in st:
                #print(str(st_original), "does not contain", str(self.T))
                return False
            else:
                st = st.replace(self.T[i], "", 1)
        #print(str(st_original), "does contain", str(self.T))
        return True

    def dp(self, win_pack):
        prior, st, i, j = win_pack

        if self.contains(st):
            return st
        else:
            if(i >= 0  or j < len(self.S)):
                if i >= 0 and j < len(self.S):

                    heappush(self.q, (prior+1, self.S[i] + st, i-1, j))
                    heappush(self.q, (prior+1, st + self.S[j], i, j+1))
                    heappush(self.q, (prior+2, self.S[i] + st + self.S[j], i-1, j+1))
                if i >= 0:
                    heappush(self.q, (prior+1, self.S[i] + st, i-1, j))
                else:
                    heappush(self.q, (prior+1, st + self.S[j], i, j+1))
            if len(self.q) > 0:
                item = heappop(self.q)
                return self.dp(item)
            else:
                return ""




    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        self.S = s
        self.T = t

        i = 0
        st = ''

        self.q = []

        while i < len(self.S):
            win_pack = (1, self.S[i], i-1, i+1)
            heappush(self.q, win_pack)

            #input s[i]
            #let dp take care of the rest
            i += 1
        st = self.dp(win_pack)
        return st


        
