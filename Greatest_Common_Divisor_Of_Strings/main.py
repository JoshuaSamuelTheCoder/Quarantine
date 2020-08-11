"""
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""



Note:

    1 <= str1.length <= 1000
    1 <= str2.length <= 1000
    str1[i] and str2[i] are English uppercase letters.
"""

class Solution(object):

    def trie_add(self, st):

        cur = self.trie
        for ch in st:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur["*"] = True

    def trie_contains(self, st):
        cur = self.trie

        for ch in st:
            if ch not in cur:
                return False
            cur = cur[ch]
        return True

    def dividesEvenly(self, str1, st):

        if len(str1) % len(st) != 0:
            return False

        if str1 == len(str1)/len(st)*st:
            return True
        return False


    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """



        if len(str1) == 0 and len(str2) == 0:
            return ""

        self.trie = {}

        self.trie_add(str2)

        final_str = ""
        rtn_str = ""
        right_p = 0
        while right_p < len(str1):
            final_str += str1[right_p]

            right_p += 1
            if self.trie_contains(final_str) and self.dividesEvenly(str1, final_str) and self.dividesEvenly(str2, final_str):
                rtn_str = final_str
        return rtn_str
        
