/*
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.



Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99


Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.

 */
int singleNumber(int* nums, int numsSize){

    int single = 0;

    for(int i = 0; i < 32; i++) {

        int count = 0;
        for(int j = 0; j < numsSize; j++) {
            if (nums[j] & (UINT32_C(1) << i)) {
                count += 1;
            }
        }
        if(count % 3 != 0) {
            single |= (UINT32_C(1) << i);
        }

    }
    return single;

}
