/*
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/
int isUnique(char *s, int cheat) {

    if(cheat < strlen(s)) {
        return cheat;
    }
    for(int i = 0; i < strlen(s); i++) {
        for(int j = i+1; j < strlen(s); j++) {
            if(s[i] == s[j]) {
                return j;
            }
        }
    }
    return strlen(s) + 1;
}

int isUnique_2(char *s) {


    for(int i = 0; i < strlen(s); i++) {
        for(int j = i+1; j < strlen(s); j++) {
            if(s[i] == s[j]) {
                return 0;
            }
        }
    }
    return 1;
}

int lengthOfLongestSubstring_h1(char * s){

    int len = 100;
    len = strlen(s);
    int maxLen = 0;
    int isUn = len;
    for(int i = 0; i < len; i++) {

        for(int j = i; j < len; j++) {


            if(j-i+1 <= maxLen ) {

                continue;
            }
            char *example = malloc(j-i+2);


            //example = &s[i];
            memcpy(example, s+i, j-i+1);
            example[j-i+1] = '\0';

            //printf(example);

            if(strlen(example) > maxLen) {
                isUn = isUnique_2(example);
                if(isUn) {
                    maxLen = strlen(example);
                }

            }
            //printf("%d is %d\n", strlen(example), isUn);
            //printf(example);

            free(example);

            //printf("\n");
        }
    }

    return maxLen;

}


int lengthOfLongestSubstring_h2(char * s){

    int len = 100;
    len = strlen(s);
    int maxLen = 0;
    int isUn = len;
    for(int i = 0; i < len; i++) {

        for(int j = len-1; j >= 0; j--) {


            if(j-i+1 <= maxLen || isUn < j-i+1) {

                continue;
            }
            char *example = malloc(j-i+2);


            //example = &s[i];
            memcpy(example, s+i, j-i+1);
            example[j-i+1] = '\0';

            //printf(example);

            if(strlen(example) > maxLen) {
                isUn = isUnique(example, isUn);
                if(isUn > strlen(example)) {
                    maxLen = strlen(example);
                }

            }
            //printf("%d is %d\n", strlen(example), isUn);
            //printf(example);

            free(example);

            //printf("\n");
        }
    }

    return maxLen;

}

int lengthOfLongestSubstring(char * s){

    if (strlen(s) > 1000) {
        return lengthOfLongestSubstring_h2(s);
    } else {
        return lengthOfLongestSubstring_h1(s);
    }
}
