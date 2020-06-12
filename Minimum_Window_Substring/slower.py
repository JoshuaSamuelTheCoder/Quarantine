class Solution(object):
    def contains(self, st_original):
        st = str(st_original)
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

    def dp(self, st, i, j):
        if self.contains(st):
            return st
        elif(i >= 0  or j < len(self.S)):
            if i >= 0 and j < len(self.S):
                st1 = self.dp(self.S[i] + st, i-1, j)
                st2 = self.dp(st + self.S[j], i, j+1)
                st3 = self.dp(self.S[i] + st + self.S[j], i-1, j+1)
                if st1:
                    return st1
                elif st2:
                    return st2
                elif st3:
                    return st3
                return ""
            if i >= 0:
                return self.dp(self.S[i] + st, i-1, j)
            else:
                return self.dp(st + self.S[j], i, j+1)
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
        minLen = float('inf')
        minStr = ""

        while i < len(self.S):
            st = self.dp(self.S[i], i-1, i+1)
            if len(st) > 0 and len(st) < minLen:
                print(st)
                minLen = len(st)
                minStr = st
            #input s[i]
            #let dp take care of the rest
            i += 1
        return minStr
