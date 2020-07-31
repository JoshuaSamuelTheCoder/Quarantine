"""
Given a 6x6 2D Array arr:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this pattern
in arr's graphical representation:


a b c
  d
e f g

There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values.
Calculate the hourglass sum for every hourglass in arr then print the maximum hourglass sum.

For example, given the 2D array:

-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

We calculate the following 16 hourglass values:

-63, -34, -9, 12,
-10, 0, 28, 23,
-27, -11, -2, 10,
9, 17, 25, 18

Our highest hourglass value is 28 from the hourglass:

0 4 3
  1
8 6 6
"""

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def compute_hg(arr, row, col):
    sum_hg = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col + 2):
            if i == row and (j == col-1 or j == col+1):
                continue
            else:
                sum_hg += arr[i][j]
    return sum_hg

def hourglassSum(arr):

    sum_arr = float("-inf")
    for row in range(1,len(arr)-1):
        for col in range(1, len(arr[row])-1):
            sum_arr = max(compute_hg(arr,row,col), sum_arr)

    return sum_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
