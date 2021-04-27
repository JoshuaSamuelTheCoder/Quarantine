#include <stdio.h>
#include <string.h>
/*
Maximum consecutive repeating character in string

Given a string, the task is to find the maximum consecutive
repeating character in a string.
Note: We do not need to consider the overall count,
but the count of repeating that appears in one place.
Examples:

Input : str = "geeekk"
Output : e

Input : str = "aaaabbcbbb"
Output : a
*/

char maxConsecutiveChar(char * s) {

  int length = strlen(s);
  if (length == 1) {
    return s[0];
  }

  char maxChar = s[0];
  int maxCount = 1;
  char contestChar = s[0];
  int count = 1;
  char ch;
  for(int i = 1; i < length; i++) {
    ch = s[i];
    if(ch == contestChar) {
      count++;
    } else {
      if(count > maxCount) {
        maxChar = contestChar;
        maxCount = count;
      }
      contestChar = ch;
      count = 1;
    }
  }
  return maxChar;
}


int main() {
    char s1[] = "geeekk";
    char s2[] = "aaaabbcbbb";
    printf("%c\n",maxConsecutiveChar(s1));
    printf("%c\n",maxConsecutiveChar(s2));
    return 0;
}
  
