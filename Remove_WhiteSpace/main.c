#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char* removeWhiteSpace(char *s) {
  //hello interviewer  -> hellointerviewer

  if (s == NULL) {
    return s;
  }
  int length = strlen(s);
  if (length <= 1) {
    return s;
  }

  int index = -1;
  for(int i = 0; i < length; i++) {
    char ch = s[i];
    if (ch == ' ' && index == -1) {
      index = i;
    } else if (ch != ' ' && index != -1) {
      s[index] = ch;
      index++;
    }
  }

  s[index] = '\0';
  /*
  while (index < length) {
    s[index] = ' ';
    index++;
  }
  */
  return s;
}

int main() {
    char *s = (char *) malloc(sizeof(char)*20);
    strcpy(s, "hello interv iewer ");
    printf("%s", removeWhiteSpace(s));
    return 0;
}
