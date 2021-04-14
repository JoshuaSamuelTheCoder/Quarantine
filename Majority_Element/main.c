/*
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
*/

#include <stdio.h>

int majority_element(int *nums, int numsSize) {
    int count = 1;
    int curr_val = nums[0];

    for(int i = 0; i < numsSize; i++) {

        if(nums[i] == curr_val) {
            count += 1;
        } else {
            count--;
            if (count == 0) {
                curr_val = nums[i];
                count = 1;
            }
        }
    }
    count = 0;
    for(int i = 0; i < numsSize; i++) {
      if (nums[i] == curr_val) {
        count++;
      }
    }
    if(count <= numsSize/2) {
      return -1;
    }
    return curr_val;
}


int main() {
    int arr[] = {3, 3, 4, 2, 4, 4, 2, 4, 4};
    //int arr[] = {3, 3, 4, 2, 4, 4, 2, 4};
    int length = sizeof(arr)/sizeof(int);
    printf("%d", majority_element(arr,length));
    return 0;
}
