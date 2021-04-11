#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>

/*
Given two matrices, the task to multiply them. Matrices can either be square or rectangular.

Examples:

Input : mat1[][] = {{1, 2},
                   {3, 4}}
        mat2[][] = {{1, 1},
                    {1, 1}}
Output : {{3, 3},
          {7, 7}}
Input : mat1[][] = {{2, 4},
                    {3, 4}}
        mat2[][] = {{1, 2},
                    {1, 3}}
Output : {{6, 16},
          {7, 18}}
*/

int* multiplyMatrix(int *arr1, int *arr2, int m1, int n1, int m2, int n2) {
  //m x n, n x p
  if (n1 != m2) {
    return NULL;
  }
  int* rtn_array = (int*) malloc(sizeof(int)*m1*n2);
  if (rtn_array == NULL) {
    return NULL;
  }
  int index = 0;

  int left_i = 0;
  int right_i = 0;
  int left_j = 0;
  int right_j = 0;
  int count = 0;

  for(int i = 0; i < m1*n2; i++) {
    int mulsum = 0;
    int left = 0;
    int right = 0;
    for(int j = 0; j < m2; j++) {
      left = *(arr1 + left_i*n1 + left_j);
      right = *(arr2 + right_j*n2 + right_i);
      mulsum += left*right;
      left_j++;
      right_j++;
    }
    rtn_array[index] = mulsum;
    index++;
    mulsum = 0;
    count++;
    right_i++;
    if (count % n2 == 0) {
      left_i++;
      right_i = 0;
    }
    left_j = 0;
    right_j = 0;

  }

  return rtn_array;
}

void printArr(int *arr, int rows, int cols) {
  if (rows == 0) {
    return;
  }
  for (int i = 0; i < rows; i++) {
    for(int j = 0; j < cols; j++) {
      printf("%d ", *(arr + cols*i + j));
    }
    printf("\n");
  }
}


int main() {
    int length1m = 4, length1n = 2;
    int length2m = 2, length2n = 3;
    //int test1[][2] = {{-3,-2}, {2,-1}};
    //int test2[][4] = {{-3,1,-4,3}, {5,2,4,-2}};
    int test1[][2] = {{-4,5}, {0,1}, {-3,3}, {2,4}};
    int test2[][3] = {{-2,-1,5}, {6,0,7}};
    //int test1[][2] = {{2,4}, {3,4}};
    //int test2[][2] = {{1,2}, {1,3}};


    int *answer = multiplyMatrix((int*)test1, (int*)test2, length1m,length1n,length2m,length2n);
    printArr((int*)answer, length1m, length2n);

    free(answer);
    return 0;
}
