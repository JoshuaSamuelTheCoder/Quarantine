#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*
Print all maxima in an array.

Maxima is an element at index i, such that
array[i] > array[i-1] and array[i] > array[i+1].

Example:
Input: [5,3,8,7,10]
Output: {5,8,10}

*/

int* maxima(int *arr, int arrSize, int* rtn_length) {

  int *rtn_array = (int *)calloc(arrSize, sizeof(int));
  int count = 0;
  for(int i = 0; i < arrSize; i++) {
    bool isMaxima = true;
    for(int j = i-1; j <= i+1; j+=2) {
      if (j >= 0 && j < arrSize) {
        if (arr[j] >= arr[i]) {
           isMaxima = false;
        }
      }
    }
    if (isMaxima) {
      rtn_array[count] = arr[i];
      count++;
    }

  }
  if(count < arrSize) {
    rtn_array = realloc(rtn_array, count);
  }
  *rtn_length = count;


  return rtn_array;
}

int main() {

    int arr[] = {5,3,8,4,10};
    int length = sizeof(arr)/sizeof(int);
    int *new_length = (int*)malloc(sizeof(int));
    int *rtn_arr = maxima(arr, length,new_length);

    for(int i =0; i < *new_length; i++) {
      printf("%d ", rtn_arr[i]);
    }
    printf("\n");

    return 0;
}
  
