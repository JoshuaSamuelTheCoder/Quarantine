"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"
"""

class Solution(object):
    def isSubsetFreq(self, t, s):
        #checks if a is a subset of b

        for k,v in t.items():
            if s.get(k, 0) < v:
                return False
        return True

    def isFreqZero(self, s):
        #checks if a is a subset of b

        for v in s.values():
            if v < 0:
                return False
        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        #hashmap of character counts, key: char, val: frequency  #ADO -> A:1, D:1, O:1
        #store t
        #iterate through s
        if len(s) < len(t):
            return ""

        if len(t) == 1 and t in s:
            return t

        s_freq = {}

        #for ch in t:
        #    t_freq[ch] = t_freq.get(ch, 0) + 1
        for ch in t:
            s_freq[ch] = s_freq.get(ch, 0) - 1

        i = 0
        while(i < len(t)):
            ch = s[i]
            s_freq[ch] = s_freq.get(ch, 0) + 1
            i += 1

        best_L = 0
        best_R = 0
        min_length = float("inf")
        #ans = self.isSubsetFreq(t_freq, s_freq)
        ans = self.isFreqZero(s_freq)

        if ans:
            best_R = len(t) - 1
            min_length = len(t)

        l = 0
        r = len(t) - 1
        optimization = False

        while l < len(s):
            win_length = r - l+1
            if win_length < len(t):
                if r < len(s) - 1:
                    r += 1
                    s_freq[s[r]] = s_freq.get(s[r], 0) + 1
                else:
                    break
                optimization = False
            else:
                #ans = self.isSubsetFreq(t_freq, s_freq)
                if not optimization:
                    ans = self.isFreqZero(s_freq)

                if not ans:
                    if r < len(s) - 1:
                        r += 1
                        s_freq[s[r]] = s_freq.get(s[r], 0) + 1
                    else:
                        break
                    optimization = False
                else:
                    if win_length < min_length:
                        min_length = win_length
                        best_L = l
                        best_R = r
                    s_freq[s[l]] = s_freq.get(s[l], 0) - 1
                    ans = ans and s_freq[s[l]] >= 0
                    l += 1
                    optimization = True

        if best_R == 0:
            return ""
        if best_R - best_L+1 >= len(t):
            return s[best_L: best_R+1]

        return ""
