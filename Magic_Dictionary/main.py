"""
We want to implement a data structure that will be intialized with a list of distinct strings, then you will be given another string and you should find if you can change exactly one letter of this string to match any string in the data structure.

Implement the MagicDictionary class:

MagicDictionary() Initializes the object.
void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
bool search(String searchWord) Returns true if you can change exactly one character in word to match any string in the data structure, otherwise returns false.


Example 1:

Input
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
Output
[null, null, false, true, false, false]

Explanation
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False


Constraints:
    1 <= dictionary.length <= 100
    1 <= dictionary[i],length <= 100
    dictionary[i] consist of only lower-case English letters.
    All strings in dictionary are distinct.
    1 <= searchWord.length <= 100
    searchWord consist of only lower-case English letters.
    At most 100 calls will be made to search and buildDict.
"""
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for word in dictionary:

            cur = self.trie
            for ch in word:
                if ch not in cur:
                    cur[ch] = {}
                cur = cur[ch]
            cur["*"] = True

    def search_helper(self, cur, word, i, hasTrumpCard):

        while i < len(word):
            ch = word[i]
            if hasTrumpCard:
                i += 1
                ans = False
                new_cur = cur
                for k in cur.keys():
                    if k != "*":
                        hasTrumpCard = True if k == ch else False

                        new_ans, new_cur = self.search_helper(cur[k], word, i, hasTrumpCard)
                        ans = ans or new_ans
                        if ans:
                            break
                cur = new_cur
                if ans:
                    return ans, cur
                elif len(cur) == 1:
                    return False, cur
                else:
                    continue
            elif ch not in cur:
                return False, cur
            cur = cur[ch]
            i += 1

        if "*" in cur and not hasTrumpCard:
            return True, cur
        return False, cur

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        ans, cur = self.search_helper(self.trie, searchWord, 0, True)
        return ans

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
