"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words such that:

The first word in the sequence is beginWord.
The last word in the sequence is endWord.
Only one letter is different between each adjacent pair of words in the sequence.
Every word in the sequence is in wordList.
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog" with 5 words.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no possible transformation.
"""

from collections import deque
class Solution(object):

    def isValid(self, x, y):
        #obsolete function
        count = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
            if count > 1:
                return False
        return count == 1

    def getNeighbors(self, x):
        neighbors = []
        for i in range(len(x)):
            for c in ascii_lowercase:
                newWord = x[:i] + c + x[i+1:]
                if newWord in self.wordList:
                    self.wordList.remove(newWord)
                    neighbors.append(newWord)

        return neighbors

    def bfs(self):
        while len(self.q) > 0:
            item, freq = self.q.popleft()

            neighbors = self.getNeighbors(item)
            for n in neighbors:
                if n == self.end:
                    return freq + 2
                else:
                    self.q.append((n, freq+1))
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        self.wordList = set(wordList)
        self.seen = set()
        self.q = deque()
        self.end = endWord
        self.q.append((beginWord, 0))
        return self.bfs()
