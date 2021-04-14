#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 10000

bool twoSum(int *arr, int arrSize, int target) {
  int seen[MAX] = {0};
  int temp;
  for(int i = 0; i < arrSize; i++) {
    temp = target - arr[i];
    if (seen[temp] > 0) {
      return true;
    }
    seen[arr[i]] = 1;
  }
  return false;
}

int main() {
    int t[] = {0, -1, 2, -3, 1};
    int length = (int)sizeof(t)/sizeof(int);
    printf("%d", twoSum(t, length,-2));
    return 0;
}
