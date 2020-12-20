"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
"""

class Solution(object):
    def checkPossibilityHelper(self, j, nums):

        for i in range(j, len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            else:
                return False
        return True

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True

        one_move = True

        if nums[0] > nums[1]:
            one_move = False
            nums[0] = nums[1] - 1

        for i in range(1, len(nums)):

            if nums[i] >= nums[i-1]:
                continue
            elif not one_move:
                return False
            else:
                one_move = False
                temp = nums[i-1]
                nums[i-1] = nums[i-2] if i > 1 else float("-inf")
                left = self.checkPossibilityHelper(i, nums)

                if left:
                    return left
                else:
                    nums[i-1] = nums[i] = temp
                    return self.checkPossibilityHelper(i+1, nums)

        return True
