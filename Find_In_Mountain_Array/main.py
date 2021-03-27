"""
(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.



Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
"""

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def searchMountain(self, target, mountain_arr, l, r, flip):

        #l = 0, r = center_index
        old_val = None
        while(l < r):
            mid = (l+r)//2
            mid_val = mountain_arr.get(mid)
            if mid_val < target:
                if not flip:
                    l = mid
                else:
                    r = mid
            elif mid_val > target:
                if not flip:
                    r = mid
                else:
                    l = mid
            else:
                return mid
            if mid_val == old_val:
                break
            old_val = mid_val

        return float("inf")

    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        #devise algorithm to find top of mountain
        length = mountain_arr.length()
        l,r = 0,length-1


        while(l < r):
            mid = (l+r)//2

            mid_val = mountain_arr.get(mid)
            left_val = mountain_arr.get(mid-1)
            right_val = mountain_arr.get(mid+1)

            if left_val < mid_val > right_val:
                break

            if left_val < mid_val < right_val:
                l = mid
            else:
                r = mid
        possibilities = []
        possibilities.append(self.searchMountain(target, mountain_arr, 0, mid, 0))
        possibilities.append(self.searchMountain(target, mountain_arr, mid-1, length, 1))

        sol = min(possibilities)
        if sol == float("inf"):
            sol = -1

        return sol
