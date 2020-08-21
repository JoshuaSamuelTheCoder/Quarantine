"""
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words spearted by spaces. You need to replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root with the shortest length.

Return the sentence after the replacement.



Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
Example 3:

Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
Output: "a a a a a a a a bbb baba a"
Example 4:

Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 5:

Input: dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
Output: "it is ab that this solution is ac"


Constraints:
    1 <= dictionary.length <= 1000
    1 <= dictionary[i].length <= 100
    dictionary[i] consists of only lower-case letters.
    1 <= sentence.length <= 10^6
    sentence consists of only lower-case letters ans spaces.
    The number of words in sentence is in the range [1, 1000]
    The length of each word in sentence is in the range [1, 1000]
    Each two words in sentence will be separted by exactly one space.
    sentence doesn't have leading or trailing spaces.
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

    def getWord(self, word):

        cur = self.trie
        trieWord = ""
        for ch in word:
            if "*" in cur.keys():
                break
            elif ch not in cur:
                return ""
            trieWord += ch
            cur = cur[ch]

        return trieWord


    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        words = list(map(str, sentence.split()))

        for word in dictionary:
            self.addWord(str(word))

        for i, word in enumerate(words):
            newWord = self.getWord(word)
            if newWord:
                words[i] = newWord

        return " ".join(w for w in words)
