/*
Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
*/

char * reverseWords(char * s){

    if(s == NULL) {
        return s;
    }
    int length = strlen(s);
    if(length <= 1) {
        return s;
    }

    char ch;
    int index = 0;
    char new_word[length];
    char **new_s = malloc(sizeof(char*)*strlen(s));

    int s_index;

    for(int i = 0; i < length; i++) {
        ch = s[i];
        if(ch != ' ') {
            new_word[index] = ch;
            index++;
        } else if(index != 0){
            new_s[s_index] = (char*)malloc(sizeof(char)*index+2);
            strncpy(new_s[s_index], new_word, index);
            new_s[s_index][index] = ' ';
            new_s[s_index][index+1] = '\0';
            s_index++;
            index = 0;
        }
    }

    if(index != 0) {
        new_s[s_index] = (char*)malloc(sizeof(char)*index+2);
        strncpy(new_s[s_index], new_word, index);
        new_s[s_index][index] = ' ';
        new_s[s_index][index+1] = '\0';
        s_index++;
        index = 0;
    }

    char *final_s = (char*) malloc(sizeof(char)*strlen(s)+2);
    int final_index = 0;
    char space[] = " ";

    for(int i = s_index-1; i >= 0; i--) {
        if(i == 0) {
            strcpy(final_s + final_index, new_s[i]);
            final_index += strlen(new_s[i]);
            final_s[strlen(final_s) - 1] = '\0';
        } else {
            strcpy(final_s + final_index, new_s[i]);
            final_index += strlen(new_s[i]);
        }
    }

    for(int i = 0; i < s_index; i++) {
        free(new_s[i]);
    }
    free(new_s);

    return final_s;

}
