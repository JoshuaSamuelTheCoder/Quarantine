"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""

class Solution(object):

    def dp(self,i,j):

        sol = False
        if (i, j) not in self.map:
            if j == len(self.p):
                sol = i == len(self.s)
                self.map[(i,j)] = sol
            else:
                sol = False
                if self.p[j] == "*":
                    if i == len(self.s):
                        sol = self.dp(i, j+1)
                    else:
                        sol = self.dp(i, j+1) or self.dp(i+1,j)

                else:
                    dot = i < len(self.s) and self.p[j] in [self.s[i], "?"]
                    sol = (dot and self.dp(i+1, j+1))
                self.map[(i,j)] = sol


        return self.map[(i,j)]



    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """



        self.s = s
        #self.p = p
        self.p = ''.join(["*" if "*" in k else k[0]*(len(list(k[1]))) for k in groupby(p)])
        print(self.p)
        self.map = {}

        return self.dp(0,0)
