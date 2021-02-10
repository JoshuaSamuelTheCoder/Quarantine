#include <stdio.h>
#include <string.h>

/* Reverses a string in C */

void reverseString(char* s) {
    //assume null terminated

    if (s == NULL) {
        return;
    }
    int length = strlen(s);
    if (length <= 1) {
        return;
    }

    char *start = s;
    char *end = s + length -1;

    while(start < end) {

        char temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}

void reverseStringNum(char *s) {

    if (s == NULL) {
        return;
    }
    int length = strlen(s);
    if (length <= 1) {
        return;
    }

    for(int i = 0; i < length/2; ++i) {
        char temp = s[i];
        s[i] = s[length - i - 1];
        s[length - i - 1] = temp;
    }

}


void reverseStringNumP(char *s) {

    if(s == NULL) {
        return;
    }
    int length = strlen(s);
    if (length <= 1) {
        return;
    }

    for(int i = 0; i < length/2; ++i) {
        char temp = *(s + i);
        *(s + i) = *(s + length - i - 1);
        *(s + length - i - 1) = temp;
    }

}


int main() {

    char s[] = "Hello";
    reverseStringNumP(s);
    printf("%s", s);

}
