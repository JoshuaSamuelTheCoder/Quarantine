/*
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.


Note: You may assume the string contains only lowercase English letters.
*/

int firstUniqChar(char * s){

    if (s == NULL) {
        return -1;
    }
    int length = strlen(s); //assume null terminated
    if (length <= 1) {
        return length - 1;
    }
    int *seen = (int*)calloc(26, sizeof(int));


    int index = 0;

    for(int i = 0; i < length; i++) {
        index = s[i] - 'a';

        if(seen[index] == 0) {
            seen[index] = i+1;
        } else {
            seen[index] = -1;
        }
    }

    for(int i = 0; i < length; i++) {
        index = s[i] - 'a';
        if (seen[index] > 0) {
            int rtn_val = seen[index] - 1;
            free(seen);
            return rtn_val;
        }
    }
    free(seen);
    return -1;
}
