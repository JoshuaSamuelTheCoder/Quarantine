#include <stdio.h>
#include <math.h>
/*
Given two numbers A and B, the task is to count the number of set bits in A and B and flip the bits of the obtained sum.

Examples:

Input: A = 5, B = 7
Output: 2
Explanation:
Binary representation of A is 101.
Binary representation of B is 111.
Count of set bits in A and B = 2 + 3 = 5.
Binary representation of the sum obtained = 101
Flipping the bits of the sum, the number obtained is (010)2 = 2.
Therefore, the required output is 2.

Input: A = 76, B = 35
Output: 1
Explanation:
Binary representation of A is 1001100
Binary representation of B is 100011
Count of set bits in A and B = 3 + 3 = 6
Binary representation of the sum obtained = 110
Flipping the bits of the sum, the number obtained is (001)2 = 1.
Therefore, the required output is 1.
*/

unsigned int count_set_bits(unsigned int n) {
    unsigned int count = 0;
    while(n != 0) {
        n = n & (n-1);
        count += 1;
    }
    return count;

}

int flip_bits_sum(int a, int b) {

    int sum_set_bits = count_set_bits(a) + count_set_bits(b);

    int count = 1 << (int) log2(sum_set_bits);
    int mask = count | count - 1;

    return sum_set_bits^mask;
}

int main() {
    printf("%d", flip_bits_sum(5,7));
    printf("%d", flip_bits_sum(76,35));
    return 0;
}
  
