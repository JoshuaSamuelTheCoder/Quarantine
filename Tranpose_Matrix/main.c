#include <stdio.h>
#include <stdlib.h>

/*
Transpose a matrix in place

Example 1:
1 2 3        1 4 7
4 5 6   ---> 2 5 8
7 8 9        3 6 9

Example 2:
1 2 3        1 4
4 5 6   ---> 2 5
             3 6
*/
void transposeMatrix(int *matrix, int rows, int cols) {

  for(int i = 0; i < rows; i++) {
    for(int j = i; j < cols; j++) {
      int temp = *(matrix + i*cols + j);
      *(matrix + i*cols + j) = *(matrix + j*cols + i);
      *(matrix + j*cols + i) = temp;
    }
  }

}

int main() {
    int rows = 2;
    int cols = 3;
    int matrix[2][3] = {{1,2,3}, {4,5,6}};
    for(int i = 0; i < rows; i++) {
      for(int j = 0; j < cols; j++) {
        printf("%d ", matrix[i][j]);
      }
      printf("\n");
    }
    printf("\n");
    transposeMatrix((int*)matrix, rows, cols);

    for(int i = 0; i < cols; i++) {
      for(int j = 0; j < rows; j++) {
        printf("%d ", matrix[i][j]);
      }
      printf("\n");
    }
    return 0;
}
  
