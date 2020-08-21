"""
There are N words in a dictionary such that each word is of fixed length and M consists only of lowercase English letters, that is ('a', 'b', ...,'z')
A query word is denoted by Q. The length of query word is M. These words contain lowercase English letters but at some places instead of a letter between 'a', 'b', ...,'z' there is '?'. Refer to the Sample input section to understand this case.

A match count of Q, denoted by match_count(Q) is the count of words that are in the dictionary and contain the same English letters(excluding a letter that can be in the position of ?) in the same position as the letters are there in the query word Q. In other words, a word in the dictionary can contain any letters at the position of '?' but the remaining alphabets must match with the query word.


You are given a query word Q and you are required to compute match_count.


Input Format

The first line contains two space-separated integers N and M denoting the number of words in the dictionary and length of each word respectively.
The next N lines contain one word each from the dictionary.
The next line contains an integer Q denoting the number of query words for which you have to compute match_count.
The next Q lines contain one query word each.

Output Format
For each query word, print match_count for a specific word in a new line.

Constraints

1 <= N <= 5X10^4
1 <= M <= 7
1 <= Q <= 10^5
"""

class Solution(object):
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        cur = self.trie
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur["*"] = True

    def search_helper(self, word, cur, i):
        while i < len(word):
            ch = word[i]
            if ch == "?":
                lst_ch = cur.keys()
                ans = 0
                i += 1
                for c in lst_ch:
                    new_ans = self.search_helper(word, cur[c], i)
                    ans += new_ans
                return ans
            elif ch not in cur:
                return 0
            cur = cur[ch]
            i += 1
        if "*" in cur:
            return 1
        else:
            return 0

    def search(self, word):
        return self.search_helper(word, self.trie, 0)

if __name__ == "__main__":
    sol = Solution()
    sol.addWord("cat")
    sol.addWord("map")
    sol.addWord("bat")
    sol.addWord("man")
    sol.addWord("pen")

    lst = ["?at", "ma?", "?a?", "??n", ""]
    for word in lst:
        print(word + " is: " + str(sol.search(word)))
