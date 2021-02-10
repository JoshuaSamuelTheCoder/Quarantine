#include <stdio.h>
#include <string.h>
#include <stdint.h>

int getKthSortedElement(int *a1, int *a2, int len1, int len2, int k) {

    int i = 0;
    int j = 0;

    int index = 1;

    while (i < len1 || j < len2) {

        if (i < len1 && j < len2) {
            if (a1[i] < a2[j]) {
                if (index == k) {
                    return a1[i];
                }
                i += 1;
            } else {
                if (index == k) {
                    return a2[j];
                }
                j += 1;
            }
        } else if(i < len1) {
            if (index == k) {
                    return a1[i];
            }
            i += 1;
        } else if(j < len2) {
            if (index == k) {
                return a2[j];
            }
            j += 1;
        }
        index += 1;
    }

    return -1;


}


int main() {

    int a1[4] = {1,2,3,4};
    int a2[4] = {5,6,7,8};

    int len1 = sizeof(a1)/sizeof(int);
    int len2 = sizeof(a2)/sizeof(int);

    printf("%d\n", getKthSortedElement(a1, a2, len1, len2, 8));

}
