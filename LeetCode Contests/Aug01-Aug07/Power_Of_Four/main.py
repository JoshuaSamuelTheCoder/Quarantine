"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true

Example 2:

Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?
"""
#Note: I didn't solve this myself I had to look it up
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num != 0 and ((num & (num - 1)) == 0) and not (num & 0xAAAAAAAA))
