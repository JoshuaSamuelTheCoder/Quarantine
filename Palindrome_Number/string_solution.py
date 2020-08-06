"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Could you solve it without converting the integer to a string? No
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        s = str(x)
        l_pointer = 0
        r_pointer = len(s)-1

        while(l_pointer < r_pointer):
            if s[l_pointer] != s[r_pointer]:
                return False
            l_pointer += 1
            r_pointer -= 1


        return True
