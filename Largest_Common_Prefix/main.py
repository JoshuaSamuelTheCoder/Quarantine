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

class Solution(object):
    #Trie solution: O(n*len(str))
    #Iteration solution (O(len(str)*n + n))
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minStr = ""
        minVal = float("inf")
        for s in strs:
            if len(s) < minVal:
                minStr = s
                minVal = len(s)

        rtn_st = ""

        for i, ch in enumerate(minStr):
            equal = True
            for j in range(len(strs)):
                if ch != strs[j][i]:
                    equal = False
                    break
            if not equal:
                break
            rtn_st += ch
        return rtn_st
