#include <stdio.h>


int getIthBits(int n, int lsb, int width) {

    int val = n >> (lsb);
    int mask = (1 << width) - 1;
    return mask & val;

}

int main() {
    //111010, 2, 3 -> 110
    printf("%d", getIthBits(58, 2, 3));
    return 0;
}
