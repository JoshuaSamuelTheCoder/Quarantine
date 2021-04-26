/*
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.



Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]


Constraints:
    1 <= arr1.length, arr2.length <= 1000
    0 <= arr1[i], arr2[i] <= 1000
*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>

#define MAX 1001

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int* relativeSortArray(int* arr1, int arr1Size, int* arr2, int arr2Size, int* returnSize){

    //for each element in arr2:
    // count frequency in arr 1

    int freq[MAX] = {0};
    int freq2[MAX] = {0};

    for(int i = 0; i < arr2Size; i++) {
        freq2[arr2[i]] += 1;
    }

    int *remaining = (int *)malloc(sizeof(int)*arr1Size);
    int r_index = 0;
    for(int i = 0; i < arr1Size; i++) {
        freq[arr1[i]] += 1;
        if(freq2[arr1[i]] == 0) {
            remaining[r_index] = arr1[i];
            r_index++;
        }
    }

    int *rtn_array = (int *)malloc(sizeof(int)*arr1Size);
    int index = 0;
    for(int i = 0; i < arr2Size; i++) {
        for(int j = 0; j < freq[arr2[i]]; j++) {
            rtn_array[index] = arr2[i];
            index++;
        }
    }

    qsort(remaining, r_index, sizeof(int), cmpfunc);
    for(int i = 0; i < r_index; i++) {
        rtn_array[index] = remaining[i];
        index++;
    }

    *returnSize = arr1Size;
    return rtn_array;
}
