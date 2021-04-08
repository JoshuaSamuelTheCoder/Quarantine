#include <stdio.h>
#include <stdlib.h>
/*
Write function to flip array a[10,10] along diagonal line from a[0,0] to a[9,9]
Define and init array (0…..99) in main()
Call flip function in main and print the results
Use IDE you prefer to test / debug

e.g. a[0,1] <-> a[1,0],  a[0,2] <-> a[2, 0], …….a[9,0] <-> a[0,9]
1, 2, 3				1, 4, 7
4, 5, 6				2, 5, 8
7, 8, 9				3, 6, 9

1, 2, 3              //1,0 1,1, 1,2
4  5  6                //0,1, 1,0 2,0
7
*/
void arraySwap(int **arr, int size) {
  int k = 0;
  for(int i = 0; i < size; i++) {
    for(int j = k; j < size; j++) {
      int temp = arr[i][j]; //
      arr[i][j] = arr[j][i];
      arr[j][i] = temp;
    }
    k++;
  }
}

int main() {
  int count = 0;
  int size = 10;

  //initialize
  int **a = (int**) malloc(size*sizeof(int*));

  for(int i = 0; i < size; i++) {
    a[i] = (int *) malloc(size*sizeof(int));
  }
  //set 2D array to 1....100
  for(int i = 0; i < size; i++) {
    for(int j = 0; j < size; j++) {
      a[i][j] = count;
      count++;
    }
  }
  arraySwap(a, 10);
  //print elements after swap
  for(int i = 0; i < size; i++) {
    for(int j = 0; j < size; j++) {
      printf("%d ", a[i][j]);
    }
    printf("\n");
  }
  //free memory
  for(int i = 0; i < size; i++) {
    free(a[i]);
  }
  free(a);

  return 0;
}
