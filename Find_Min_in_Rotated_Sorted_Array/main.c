int findMin(int* nums, int numsSize){
    if (numsSize == 0) {
        return -1;
    }
    int sol = nums[0];
    int value = nums[0];
    for(int i = 1; i < numsSize; i++) {
        if (nums[i] < value) {
            return nums[i];
        }
        value = nums[i];
    }
    return sol;
}
