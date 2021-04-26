#include <stdio.h>
#include <stdint.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

/*
SleepSort (A Horrible, Horrible Algorithm)

Given some integers we want to sort e.g. 3,1,5,4,2

-create a new thread for each integer
-inside the thread, sleep for the integer's value
-add the integer to a resulting collection

Once all the threads done running, the resulting
collection will contain the integers in sorted order.
(Can you explain how they will end up sorted?)

Let's Implement! You're free to look up questions on
Google, StackOverflow, etc.

Imagine this is a normal work day, use all tools
available to you.

Hint: Get a first iteration running, iterate and
improve afterwards.
*/
int *global_lst;
static int index;

void* insertNumber(void *arg) {
  int *val_to_sleep = (int *)arg;
  sleep(*val_to_sleep);
  static int index;
  global_lst[index] = *val_to_sleep;
  printf("%d\n", *val_to_sleep);
  index++;
  return NULL;
}

int main() {

    int arr[] = {3, 1, 5, 4, 2};
    global_lst = (int*)malloc(sizeof(arr));
    int length = sizeof(arr)/sizeof(int);

    pthread_t tid[length];

    for(int i = 0; i < length; i++) {
      pthread_create(&tid[i], NULL, insertNumber, (void*) (arr + i));
    }

    for(int i = 0; i < length; i++) {
      pthread_join(tid[i], NULL);
    }

    printf("Done, Final Array is:\n");
    for(int i = 0; i < length; i++) {
      printf("%d\n", global_lst[i]);
    }

    return 0;
}
