#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


//"Lord is Great" -> "droL si taerG"
void reverseWord(char *s, int l, int r) {

  while(l < r) {
        char temp = s[l];
        s[l] = s[r];
        s[r] = temp;
        l++;
        r--;
  }
}

char* reverseWords(char *s) {

  if (s == NULL) {
    return s;
  }
  int length = strlen(s);
  if (length <= 1) {
    return s;
  }

  int begin = 0;
  int end = 0;
  for(int i = 0; i < length; i++) {
    char ch = s[i];
    if (ch != ' ') {
      end += 1;
    } else {
      int l = begin;
      int r = end - 1;
      reverseWord(s, l, r);

      begin = i + 1;
      end = i+1;
    }
  }
  reverseWord(s, begin, end - 1);
  return s;
}

int main() {
    char *s = (char *)malloc(sizeof(char)*13);
    strcpy(s, "Lord is Great");
    printf("%s", reverseWords(s));
    free(s);
    return 0;
}
