
#define MAX(A,B)((A) >= (B)? (A): (B))

int secondLargestElement(int *arr, int arrSize) {

  int first_max = INT_MIN;
  int second_max = INT_MIN;

  for(int i = 0; i < arrSize; i++) {
    //greater than first_max
    //less than first_max, greater than second_max
    //neither
    if(arr[i] > first_max) {
      second_max = first_max;
      first_max = arr[i];
    } else if(arr[i] > second_max && arr[i] != first_max) {
      second_max = arr[i];
    }
  }
  if (second_max == INT_MIN) {
    return -1;
  }

  return second_max;

}


int main() {
    //int test[] = {12, 35, 1, 10, 34, 1};
    //int test[] = {10, 5, 10};
    int test[] = {10, 10, 10};
    int length = (int) sizeof(test)/sizeof(int);
    printf("%d", secondLargestElement(test, length));
    return 0;
}
