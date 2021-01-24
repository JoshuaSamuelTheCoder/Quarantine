"""
Write an efficient program to count number of 1s in binary representation of an integer.

Examples :

Input : n = 6
Output : 2
Binary representation of 6 is 110 and has 2 set bits

Input : n = 13
Output : 3
Binary representation of 13 is 1101 and has 3 set bits
"""


class Solution(object):
    def countBits(self, num):
        count = 0
        while num > 0:
            count += num & 1
            num >>= 1
        return count



if __name__ == "__main__":
    ans = Solution()
    t1 = 6
    t2 = 13

    print(ans.countBits(6) == 2)
    print(ans.countBits(13) == 3)
