/*
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
*/

void moveZeroes(int* nums, int numsSize){

    if(nums == NULL || numsSize <= 1) {
        return numsSize;
    }

    int index = -1;
    int zeroCount = 0;

    //Ex: [0,1,0,3,12]
    for(int i = 0; i < numsSize; i++) {
        if(index == -1 && nums[i] == 0) {
            index = i;
            zeroCount++;
        } else if (index != -1 && nums[i] != 0) {
            nums[index] = nums[i];
            index++;
        } else if (nums[i] == 0) {
            zeroCount++;
        }
    }
    //[1,3,12,...]
    //zeroCount = 2
    for(int i = 0; i < zeroCount; i++) {
        nums[index] = 0;
        index++;
    }
    //[1,3,12,0,0]

    if(index == -1) {
        return numsSize;
    }

    return index;
}
