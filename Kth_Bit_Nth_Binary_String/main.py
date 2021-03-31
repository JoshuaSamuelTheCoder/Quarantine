"""
Given two positive integers n and k, the binary string  Sn is formed as follows:

S1 = "0"
Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first 4 strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.



Example 1:

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001". The first bit is "0".
Example 2:

Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001". The 11th bit is "1".
Example 3:

Input: n = 1, k = 1
Output: "0"
Example 4:

Input: n = 2, k = 3
Output: "1"
"""

class Solution(object):
    def __init__(self):
        self.flip_dict = {"0":"1", "1":"0"}

    def reverse(self, s):
        return s[::-1]

    def flip(self, s):
        new_s = ""
        for ch in s:
            new_s += self.flip_dict[ch]
        return new_s

    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s = "0"
        if n == 1:
            return s

        for i in range(1, n+1):
            new_s = s + "1" + self.reverse(self.flip(s))
            s = new_s

        return s[k-1]
