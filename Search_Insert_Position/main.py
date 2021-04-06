"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0

Constraints:
nums contains distinct values sorted in ascending order.
"""

#binary search target -> index,
#l,r
def findIndex(arr, target):

     l, r = 0, len(arr)-1
     ans = 0
     prev_element = None
     while(l < r):
         mid = (l+r)//2
         if arr[mid] == prev_element:
             break
         prev_element = arr[mid]
         if arr[mid] > target:
             r = mid
         elif arr[mid] < target:
             l = mid
         else:
             return mid
     #l,r
     if arr[l] < target and arr[r] > target:
         return r
     if arr[l] < target and arr[r] < target:
         return r+1
     elif arr[l] > target:
         return l

 if __name__ == "__main__":
     print(findIndex([1,3,5,6], 5))
     print(findIndex([1,3,5,6], 2))
     print(findIndex([1,3,5,6], 7))
     print(findIndex([1,3,5,6], 0))
     print(findIndex([1], 0))
