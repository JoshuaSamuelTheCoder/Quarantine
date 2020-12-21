"""
Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.



Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
Example 3:

Input: s = "j?qg??b"
Output: "jaqgacb"
Example 4:

Input: s = "??yw?ipkj?"
Output: "acywaipkja"
"""

class Solution(object):

    def getUniqueLetter(self, letter1, letter2):

        for i in range(97, 123):
            ch = chr(i)
            if ch != letter1 and ch != letter2:
                return str(ch)


    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        rtn_st = ""
        seen = set()
        if len(s) == 1:
            return "a"


        for i in range(len(s)):
            if s[i] == "?":
                if i == 0:
                    rtn_st += self.getUniqueLetter("", s[i+1])
                elif i == len(s) - 1:
                    rtn_st += self.getUniqueLetter(rtn_st[i-1], "")
                else:
                    rtn_st += self.getUniqueLetter(rtn_st[i-1], s[i+1])
            else:
                rtn_st += s[i]

        return rtn_st
