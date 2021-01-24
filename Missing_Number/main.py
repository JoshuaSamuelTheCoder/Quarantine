"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2

Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Example 3:
Input: [1, 2, 4, 6, 3, 7, 8]
Output: 5

Example 4:
Input: [1, 2, 3, 5]
Output: 4

Example 5:
Input: nums = [7,8,9,11,12]
Output: 10

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_n = float("inf")
        max_n = float("-inf")
        sum_n = 0
        count = 0
        for n in nums:
            if n >= 0:
                sum_n += n
                min_n = min(min_n, n)
                max_n = max(max_n, n)
                count += 1

        expected_sum = (min_n + max_n)*(max_n - min_n + 1)//2

        return expected_sum - sum_n

if __name__ == "__main__":
    ans = Solution()
    a = ans.firstMissingPositive([7,8,9,11,12])
    print(a)
