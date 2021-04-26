"""
Given a string, reverse it such that the words are in opposite order but the
letters are not

Examples:

Input: s = “geeks quiz practice code”
Output: s = “code practice quiz geeks”

Input: s = “getting good at coding needs a lot of practice”
Output: s = “practice of lot a needs coding at good getting”

Input: s = "i love programming very much"
Output: s = "much very programming love i"
"""

class Solution(object):
    def reverseWords(self, s):
        lst = list(s.split(" "))
        return " ".join(lst[::-1])


if __name__ == "__main__":
    ans = Solution()

    t1 = ["i love programming very much", "much very programming love i"]
    t2 = ["getting good at coding needs a lot of practice", "practice of lot a needs coding at good getting"]

    print(ans.reverseWords(t1[0]) == t1[1])
    print(ans.reverseWords(t2[0]) == t2[1])
