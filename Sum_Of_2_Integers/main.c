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

    //a: 01
    //b: 10

    int rtn_val = 0;
    int carry = 0;

    for(int i = 0; i < 32; i++) {

        int a_val = (a >> i) & 1;
        int b_val = (b >> i) & 1;

        if (a_val && b_val && carry) {
            rtn_val |= (1UL << i);
        } else if (a_val && b_val && !carry) {
            carry = 1;
        } else if (a_val || b_val) {

            if(!carry) {
                rtn_val |= (a_val | b_val) << i;
            }

        } else {
            rtn_val |= carry << i;
            carry = 0;
        }
    }

    return rtn_val;

}
