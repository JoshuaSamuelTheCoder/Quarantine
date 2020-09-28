"""
Given a list of items in groups, perform certain operations in order to satisfy
the constraints required by packaging automation.

    1. The first group must contain 1 item only
    2. For all other groups, the difference between the number of items in adjacent
       groups must not be greater than 1. In other words: arr[i] - arr[i-1] <= 1.

To accomplish this, the following operations are available:
    1. Rearrange the groups in any way.
    2. Reduce any group to any number that is at least 1.

Write an algorithm to find the maximum number of items that can be packaged in the
last group with the conditions in place.

Input:
The function/method consists of 2 arguments:
    numGroups: an integer representing the number of groups (n)
    arr: a list of integers representing the number of items in each groups

Output:
Return an integer representing the maximum items that can be packaged for the final
group of the list given the conditions above.

Constraints:
1 <= numGroups <= 10^5
1 <= arr[i] <= 10^9
0 <= i < numGroups

Examples:
    Example 1:
    Input:
        numGroups = 4
        arr = [3,1,3,4]
    Output:
        4
    Explanation:
        Subtract 1 from the first group, making the list [2,1,3,4]
        Rearrange the list onto [1,2,3,4]
        The final maximum of items that can be packaged in the last group is 4.

    Example 2:
    Input:
        numGroups = 4
        arr = [1,1,1,1]
    Output:
        1
    Explanation:
        The final maximum of items that can be packaged in the group is 1.

TestCases:
    TestCase 1:
    Input:
        4
        [1,3,2,2]
    Output:
        3
    TestCase 2:
    Input:
        4
        [3,2,3,5]
    Output:
        4
"""
def getMaxValue(numGroups, arr):
    #WRITE YOUR CODE HERE
    arr.sort()

    arr[0] = 1
    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] > 1:
            arr[i] = arr[i-1] + 1
    return arr[-1]
