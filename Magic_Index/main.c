#include <stdio.h>

/*
A magic index in an array is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers,
write a method to find a magic index, if one exists.

Example -12, -1, 3, 3, 10  -> returns 3
Example 0, 1, 3, 4, 10     -> returns 0 or 1
input - int array
output - the magic index
*/
int findMagicIndex(int *arr, int arrSize) {

   int l = 0, r = arrSize-1;
   int mid;
   while(l <= r) {
     mid = l + (r-l)/2; //(l+r)/2

     if(arr[mid] < mid) {
       l = mid+1;
     } else if(arr[mid] > mid) {
       r = mid-1;
     } else {
       return mid;
     }
   }
   return -1;
}


int main() {
    //int arr[] = {-12,-1, 1, 3, 10};
    int arr[] = {0, 1, 3, 4, 10};
    int length = sizeof(arr)/sizeof(int);
    printf("%d\n",findMagicIndex(arr, length));
    return 0;
}
