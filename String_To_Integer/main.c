/*
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
*/

#include <limits.h>
bool isValidInt(char ch) {

    if(ch == ' ') {
        return false;
    }
    if(ch < 48 || ch > 57) {
        return false;
    }
    return true;
}

int safeAdd(int a, int b) {

    long long res = (long long) a + b;
    if (res > INT_MAX) {
        return INT_MAX;
    }
    else if (res < INT_MIN) {
        return INT_MIN;
    } else {
        return (int) res;
    }
}

int safeMultiply(int a, int b) {

    long long res = (long long) a * b;
    if (res > INT_MAX) {
        return INT_MAX;
    }
    else if (res < INT_MIN) {
        return INT_MIN;
    } else {
        return (int) res;
    }
}

int myAtoi(char *s){

    int length = strlen(s);

    int total = 0;
    int neg = 1;
    char prev = ' ';
    bool started = false;

    for(int i = 0; i < length; i++) {
        char ch = s[i];
        if(isValidInt(ch)) {
            started = true;
            total = safeAdd(safeMultiply(total, 10), neg*(int)(ch - '0'));
        } else if(ch == '-') {
            if(prev == '+' || prev == '-') {
                return 0;
            } else if(isValidInt(prev)) {
                return total;
            } else {
              neg = -1;
            }
        } else if(ch == '+') {
            if(prev == '+' || prev == '-') {
                return 0;
            } else if(isValidInt(prev)) {
                return total;
            }
        } else if(ch != ' '){
            return total;
        } else if(ch == ' ') {
            if(prev == '+' || prev == '-') {
                return total;
            } else if(started) {
                return total;
            }
        }
        prev = ch;

    }

    return total;

}
