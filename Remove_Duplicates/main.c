/*
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
*/

int removeDuplicates(int* nums, int numsSize){

    if (nums == NULL) {
        return 0;
    } else if (numsSize <= 1) {
        return numsSize;
    }

    int index = -1;
    int duplicates = 0;
    int value = nums[0];

    for(int i = 1; i < numsSize; ++i) { //[0,1,2,2,2,3,4] -> //[0,1,2,3,4]
        if (nums[i] == value) {
            if (index == -1) {
                index = i;
                duplicates = 1;
            } else {
                duplicates++;
            }
        } else {
            if(duplicates > 0) {
                nums[index] = nums[i];
                index++;
            }
        }
        value = nums[i];
    }
    /* Code to reallocate array (not necessary)
    if(index != -1 && numsSize > index) {
        nums = (int*)realloc(nums, index*sizeof(int));
    }
    */
    if (index == -1) {
        index = numsSize;
    }
    return index;
}
