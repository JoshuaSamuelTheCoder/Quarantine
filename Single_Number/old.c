
int singleNumber(int* nums, int numsSize){
    int freq = 0;

    for(int i = 0; i < numsSize; ++i) {
        freq ^= nums[i];
    }
    return freq;
}
