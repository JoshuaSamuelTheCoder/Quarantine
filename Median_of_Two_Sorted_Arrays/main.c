/*
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
*/

#include <limits.h>
#define NUM_LISTS 2

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){


    int totalSize = nums1Size + nums2Size;
    int checkMedian;
    int medianDivide;
    if(totalSize % 2 == 0) {
        checkMedian = totalSize/2 - 1;
        medianDivide = 2;
    } else {
        checkMedian = totalSize/2;
        medianDivide = 1;
    }

    int i = 0, j = 0;
    int counter = 0;
    int rtn_vals[NUM_LISTS] = {0};
    int index = 0;

    while(i < nums1Size || j < nums2Size) {

        int v1 = INT_MAX;
        int v2 = INT_MAX;

        if(i < nums1Size) {
            v1 = nums1[i];
        }
        if(j < nums2Size) {
            v2 = nums2[j];
        }

        int val;
        if(v1 <= v2) {
            val = nums1[i];
            i++;
        } else {
            val = nums2[j];
            j++;
        }
        if (counter >= checkMedian) {
            if(totalSize % 2 != 0) {
                rtn_vals[0] = val;
                break;
            } else {
                rtn_vals[index] = val;
                index++;
                if(index > 1) {
                    break;
                }
            }
        }
        counter++;
    }

    double rtn_val = 0;
    for(int i = 0; i < NUM_LISTS; i++) {
        rtn_val += rtn_vals[i];
    }
    rtn_val = rtn_val/medianDivide;

    return rtn_val;
}
