/*
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.



Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
Example 3:

Input: s = "a", t = "aa"
Output: "a"
Example 4:

Input: s = "ae", t = "aea"
Output: "a"
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char findDifference(char *s, char *t) {

    //array that keeps track of frequency, iterate through t, increment at proper index
    //iterate through s, decrement at proper index
    //one difference, return that difference

    if (strlen(s) == 0) {
        return t[0];
    }


    int freq[26] = {0}; //[a,b,c,d,e.....x,y,z]

    for(int i = 0; i < strlen(s); i++) {
        freq[s[i] - 'a'] += 1;
    }

    int index;
    for(int j = 0; j < strlen(t); j++) {
        index = t[j] - 'a';
        freq[index] -= 1;
        if(freq[index] < 0) {
            return t[j];
        }
    }
    return NULL;
}


int main() {
    char s1[] = "abcd";
    char t1[] =
