"""
Given a list of items in groups, perform certain operations in order to satisfy the constraints required by packaging automation.
The conditions are as followed:
1.) The first group must contain 1 item only
2.) For all other groups, the difference between number of items in adjacent groups must not be greater than 1.
    In other words for 1 <= i < n, arr[i] - arr[i-1] <= 1

To accomplish this, the following operations are available:
1.) Rearrange the groups in any way.
2.) Reduce any group to any number that is at least 1

Write an algorithm to find the maximum number of items that can be packaged in the last group with the conditions in place.

Input:
The function/method consists of two arguments:
    numGroups, an integer representing the number of groups (n):
    arr, a list of integers representing the number of items in each group
Output:
Return an integer representing the maximum items that can be packaged for the final group of the list given the conditions above.

Example 1:
    Input:
    numGroups = 4
    arr = [3,1,3,4]
    Output:
    4
    Explanation:
    Subtract 1 from the first group, making the list [2,1,3,4]
    Rearrange the list into [1,2,3,4]
    The final maximum number of items that can be packaged in the last group is 4.
Example 2:
    Input:
    numGroups = 4
    arr = [1,1,1,1]
    Output:
    1
TestCase 1:
    Input:
    4
    [1,3,2,2]
    Output:
    3
    Explanation:
    These elements can be rearranged as [1,2,2,3], which results in a maximum value of 3 for the final element as it follows the constraints.
TestCase 2:
    Input:
    4
    [3,2,3,5]
    Output:
    4
    Explanation:
    These elements can be rearranged as  [2,3,3,5]
    Then, the elements can be adjusted as [1,2,3,4]
    Therefore, the maximum value of the final element is 4
"""

def getMaxValue(numGroups, arr):
    arr.sort()

    arr[0] = 1
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            arr[i] = arr[i-1] + 1

    return arr[-1]
