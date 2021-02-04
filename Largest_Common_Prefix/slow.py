"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

#Tr(ie)ing to be fancy
class Trie(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        ch = self.trie
        for w in word:
            if w not in ch:
                ch[w] = {}
            ch = ch[w]
        ch["*"] = True

    def getPrefix(self):
        prefix = ""
        cur = self.trie
        while True:
            if "*" in cur:
                return prefix
            if len(cur) == 1:
                k = cur.keys()[0]
                prefix += k
                cur = cur[k]
            else:
                return prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        self.target = len(strs)
        trie = Trie()

        for s in strs:
            if not s:
                return ""
            trie.addWord(s)

        return trie.getPrefix()
