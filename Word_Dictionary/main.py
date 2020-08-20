"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
"""

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self.trie
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur["*"] = True


    def search_helper(self, word, cur, i):
        if word == "":
            return False, cur

        while i < len(word):
            ch = word[i]
            if ch == ".":
                lst_ch = cur.keys()
                ans = False
                i += 1
                new_cur = cur
                for c in lst_ch:
                    if c != "*":
                        new_ans, new_cur = self.search_helper(word, cur[c], i)
                        ans = ans or new_ans
                        if ans:
                            break
                cur = new_cur
                if ans == True:
                    return ans, cur
                elif ans == False and len(cur) == 1:
                    return False, cur
                else:
                    continue
            elif ch not in cur:
                return False, cur
            cur = cur[ch]
            i += 1
        if "*" in cur:
            return True, cur
        else:
            return False, cur

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        ans, cur = self.search_helper(word, self.trie, 0)
        return ans



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
