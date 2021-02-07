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
//abcabcbb
//abc, len = 3
//Solution, Sliding Window. Hashmap to keep track of window letter frequency.
// O(N) time complexity, O(N) space complexity
int getKeys(char* map, int size) {
    //O(N) operation :(
    //obsolete
    int count = 0;
    for(int i = 0; i < size; i++) {
        if (map[i] > 0) {
            count += 1;
        }
    }
    return count;

}

int getIndex(char c) {
    return c - '0' + 16;
}

int notValid(char c) {
    return getIndex(c) < 0 || getIndex(c) > 100;
}


int lengthOfLongestSubstring(char * s){

    if (s == NULL || strlen(s) == 0) {
        return 0;
    }

    char *map = (char *) calloc(101, sizeof(char));

    int left = 0;
    int right = 0;

    int k = 0;
    while(k < strlen(s)) {

        if(notValid(s[k])) {
            return 1;
        }

        int index = getIndex(s[k]);

        if (map[index] == 0) {
            map[index] += 1;
            k += 1;
            right += 1;
        } else {
            break;
        }
    }

    int maxLen = k;

    while(right < strlen(s)) {

        if(notValid(s[k])) {
            return 1;
        }

        char st = s[k];
        int index = getIndex(st);
        if (map[index] > 0) {

            if (right - left > maxLen) {
                maxLen = right - left;
            }
            map[getIndex(s[left])] -= 1;
            left += 1;
        } else {
            map[getIndex(s[right])] += 1;
            right += 1;
            k += 1;
        }
    }

    if (left < strlen(s)) {
        if (right - left > maxLen) {
            maxLen = right - left;
        }
    }
    free(map);

    return maxLen;

}
