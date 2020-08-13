"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false

Constraints:

    s consists only of printable ASCII characters.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """


        new_str = ""

        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                new_str += ch.lower()
        if len(new_str) <= 1:
            return True

        if len(new_str) % 2 == 0:
            return new_str[:len(new_str)/2] == new_str[len(new_str)/2:][::-1]
        else:
            return new_str[:len(new_str)/2] == new_str[len(new_str)/2+1:][::-1]

        
