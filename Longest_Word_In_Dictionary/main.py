"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
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

    def checkWord(self, word):

        cur = self.trie
        isConstructable = False
        for ch in word:
            if "*" not in cur and ch != word[0]:
                return 0
            cur = cur[ch]

        return len(word)


    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        for word in words:
            self.addWord(word)

        maxCount = 0
        maxWord = ""
        for word in words:
            count = self.checkWord(word)
            if count > maxCount:
                maxCount = count
                maxWord = word
            elif count == maxCount:
                maxWord = min(maxWord, word)

        return maxWord
