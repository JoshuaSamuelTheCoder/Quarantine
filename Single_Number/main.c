/*
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
*/

#include <stdio.h>

int oddTimes(int *nums, int numsSize) {

    if(numsSize == 1) {
        return nums[0];
    }

    int n = nums[0];
    for(int i = 1; i < numsSize; i++) {
        n ^= nums[i];
    }

    return n;
}


int main() {
    int arr[] = {1,2,3,2,3,1,3};
    int arr2[] = {5,7,2,7,5,2,5};
    printf("%d\n", oddTimes(arr, sizeof(arr)/sizeof(int)));
    printf("%d\n", oddTimes(arr2, sizeof(arr2)/sizeof(int)));
    return 0;
}
