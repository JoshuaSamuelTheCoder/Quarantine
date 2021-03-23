"""
A magic index in an array is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists.

Example -12, -1, 3, 3, 10      left = 0, right = 4, mid = 2      left = 0, right = 3, mid = 1
Example 0, 1, 3, 4, 10        left = 0, right = 4, mid = 2      left = 2, right = 4, mid = 3
input - int array
output - the magic index (2)
"""
#Time: O(log(N))  N -> N/2 -> N/4
#Space: O(1)
def findMagicIndex(array):

    #Element < index
    #left ->

    #Element > index
    #right <-

    left, right = 0, len(array) - 1
    i = 0
    while(left < right):
        mid = (left + right)//2
        if array[mid] < mid:
            left = mid
        elif array[mid] > mid:
            right = mid
        else:
            return mid

    return -1

def findMagicIndexBrute(array):

    for i,a in enumerate(array):
        if i == a:
            return i
    return -1


if __name__ == "__main__":
    print(findMagicIndex([-12, -1, 1, 3, 10]))
    print(findMagicIndex([0, 2, 3, 4, 5]))
    print(findMagicIndex([1, 1, 1]))
    #print(findMagicIndex([-12, -1, 3, 3, 10]))
    #This solution doesn't work for arrays with monotonic values, binary search cuts off branches incorrectly
