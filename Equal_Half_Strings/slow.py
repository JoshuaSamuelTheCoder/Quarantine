class Solution(object):
    def isVowel(self, s):
        s = s.lower()
        return s == "a" or s == "e" or s == "i" or s == "o" or s == "u"

    def countVowels(self, st):
        count = 0
        for s in st:
            if self.isVowel(s):
                count += 1
        return count
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s) // 2
        return self.countVowels(s[:length]) == self.countVowels(s[length:])
