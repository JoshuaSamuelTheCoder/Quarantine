/*
Given two integers a and b, return the sum of the two integers without using the operators + and -.



Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5


Constraints:

-1000 <= a, b <= 1000
*/
int getSum(int a, int b){

    //-12, -8            10011 10111
    // -20               01011
    //from i -> (0,31)

    int mask;
    int carry = 0;
    int cur = 0;
    int rtn_val = 0;
    for(int i = 0; i < 32; i++) {
        cur = 0;
        mask = (1UL << i);
        if ((a & mask) && (b & mask)) {
            cur = carry;
            carry = 1;
        } else if ((a & mask) || (b & mask)) {
            // a or b is 1
            if (carry) {
                cur = 0;
                carry = 1;
            } else {
                cur = 1;
                carry = 0;
            }
        } else {
            cur = carry;
            carry = 0;
        }
        rtn_val |= ((long)cur << i);
    }

    return rtn_val;

}
