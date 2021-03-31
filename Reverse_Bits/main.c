#include <stdio.h>
#include <string.h>
#include <stdlib.h>


//10000100 -> 00100001
//132 -> 33
int reverseBits(int n) {

  //10000000
  int reversed_n = 0;
  while (n != 0) {
    int last = n & 1;
    reversed_n <<= 1;
    reversed_n = reversed_n | last;
    n >>= 1;
  }
  return reversed_n;
}

int main() {
    printf("%d", reverseBits(132));
    return 0;
}
