"""
Given an array of binary digits, 0 and 1, sort the array so that all zeros are at one end
and all ones are at the other. Which end does not matter. To sort the array, swap any two
adjacent elements. Determine the minimum number of swaps to sort the array.

Example:
arr = [0,1,0,1]

With one move, switching elements 1 and 2 yields [0,0,1,1] a sorted array

Function Description:
Input:
    int arr[n]: an array of binary digits
Returns:
    int: the minimum number of moves necessary

Sample Testcase 1:
arr[i] size n = 8
arr = [1,1,1,1,0,1,0,1]
Sample Output:
3

Explanation:
Perform the following minimal sequence of 3 moves:
    [1,1,1,1,0,1,0,1] -> [1,1,1,1,1,0,0,1] -> [1,1,1,1,1,0,1,0] -> [1,1,1,1,1,1,0,0]

Sample Testcase 2:
arr[i] size n = 8
arr = [1,0,1,0,0,0,0,1]
Sample Output:
6

Explanation:
Perform the following minimal sequence of 6 moves:
    [1,0,1,0,0,0,0,1] -> [1,1,0,0,0,0,0,1] -> [1,1,0,0,0,0,1,0] -> [1,1,0,0,0,1,0,0] -> [1,1,0,0,1,0,0,0] -> [1,1,0,1,0,0,0,0] -> [1,1,1,0,0,0,0,0]
"""
def minMoves(arr):
    numZeros = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            numZeros += 1
    numOnes = len(arr) - numZeros

    onesCount = 0
    i = 0
    while i < numZeros:
        if arr[i] == 1:
            onesCount += abs(numZeros - i)
            numZeros += 1
        i += 1

    zerosCount = 0
    j = 0
    while j < numOnes:
        if arr[j] == 0:
            zerosCount += abs(numOnes - j)
            numOnes += 1
        j += 1
    return min(onesCount, zerosCount)
