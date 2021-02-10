"""
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to
target. Return the sum of the three integers. You ma assume
that each input would have exactly one solution.

Input: nums = [-1, 2, 1, -4], target = 1
Output: 2

Explanation: The sum that is closest to the target is 2.
(-1 + 2 + 1 = 2).

Assume:
-no repeated values
-cannot reuse values
"""


def closest_3sum(nums, target):

    nums.sort()
    #[-4, -1, 1, 2]
    l = 0
    r = len(nums) - 1
    closest = float("inf")

    for i,n in enumerate(nums):
        l,r = i+1, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r] + n
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return s
            lst = [s, closest]
            closest = min(lst, key = lambda x: abs(x - target))

    return closest


if __name__ == "__main__":
    print(closest_3sum([-1, 2, 1, -4], 1))
