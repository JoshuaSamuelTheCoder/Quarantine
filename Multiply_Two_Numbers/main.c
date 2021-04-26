#include <stdio.h>
#include <stdint.h>


/*
Write a function that would do multiplication of 2 numbers without using the multiplication operator using bit manipulation
*/

uint16_t multiplyBy7(uint8_t x) {
  //0111
  return (x << 2) + (x << 1) + x;
}

uint16_t multiplyBy11(uint8_t x) {
  //1011
  return (x << 3) + (x << 1) + x;
}

uint16_t mult(uint8_t x, uint8_t y) {

  int rtn_val = 0;
  int pow = 0;
  while(y != 0) {
    if (y & 1) {
      rtn += x << pow;
    }
    y >>= 1;
    pow++;
  }
  return rtn_val;
}

int main() {
    printf("%d\n", mult(2,3));
    printf("%d\n", mult(24,2));
    printf("%d\n", mult(2,24));
    printf("%d\n", mult(10,2));
    printf("%d\n", mult(0,3));
    printf("%d\n", mult(3,0));
    return 0;
}
