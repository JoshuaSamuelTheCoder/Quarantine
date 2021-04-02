#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

bool isUnique(char *s) {

  if (s == NULL) {
    return false;
  }
  int length = strlen(s);
  if (length <= 1 || length > 26) {
    return false;
  }

  //int *freq = (int *) calloc(26, sizeof(int));
  int freq = 0;

  for(int i = 0; i < length; i++) {
    int index = s[i] - 'a';
    if (freq & (1 << index)) {
      return false;
    }
    freq |= (1 << index);
    /*
    freq[index] += 1;
    if (freq[index] > 1) {
      free(freq);
      return false;
    }
    */
  }

  //free(freq);
  return true;
}


int main() {

    printf("%d\n", isUnique("car"));
    printf("%d\n", isUnique("carc"));
    return 0;
}
  
