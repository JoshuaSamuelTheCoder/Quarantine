#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

void* mallocAligned(int32_t size, int8_t alignment) {

   int div = size / alignment;
   void **p, *p_orig;

   //allocate for 2 extra segments of alignment size
   //1 for alignment
   //1 for padding
   //sizeof(void *) for storing the meta data - location of the original ptr
   //sizeof(void *) is 8 bytes

   p_orig = malloc(div*alignment + 2*alignment + sizeof(void*));
   //allocation is slightly large, could be optimized

   int rem_p = ((int) (p_orig+sizeof(void*)) % alignment);

   //the arithmetic below is done by bytes not by ptr size of 4/8 bytes
   // because the p_orig is a void*,
   // This an undefined feature of C compiler but serves its purpose for this case
   p = p_orig + sizeof(void*) + alignment - rem_p; //rem_p is either 0 or nonzero
   p[-1] = p_orig; //to retrive original pointer when its time to free

   //prints for debugging
   /*
   printf("rem_p=%d\n", rem_p);
   printf("p = %p\n", p);
   printf("&p[-1] = %p\n", &p[-1]);
   printf("p[-1] = %p\n", p[-1]);
   printf("p - 1 = %p\n", p - 1);
   printf("p_orig = %p\n", p_orig);
   printf("p_orig - 1 = %p\n", p_orig - 1);
   printf("void * size: %ld\n", sizeof(void*));
   */
   return p;
}


void mallocAlignedFree(void *p)
{
   void *p_orig = ((void**) p)[-1]; //locate original pointer
   free(p_orig);
}


int main() {

    //Tests: check for a print of zero for correctness

    printf("Testcase 1: Inputs: 13, 7\n");
    void *p = mallocAligned(13, 7);
    printf("check p address mod alignment is %x\n", (int)p%7);
    assert(((int) p % 7) == 0);
    mallocAlignedFree(p);


    printf("\n");
    printf("Testcase 2: Inputs: 6, 7\n");
    void *c = mallocAligned(6, 7);
    // check for a print of zero for correctness
    printf("check c address mod alignment is %x\n", (int)c%7);
    assert(((int) c % 7) == 0);
    mallocAlignedFree(c);


    printf("\n");
    printf("TestCase 3: Inputs: 14, 9\n");
    void *a = mallocAligned(14, 9);
    printf("check a address mod alignment is %x\n", (int)a%9);
    assert(((int) a % 9) == 0);
    mallocAlignedFree(a);

    /*
    //Additional testing measures, loops through varying sizes for a certain alignment
    int val = 7;
    printf("\n");
    for(int i = 1 ; i < 20; i++) {
      printf("Inputs: Size: %d, Alignment: %d\n", i, val);
      p = mallocAligned(i, val);
      printf("check p %x\n", (int)p%val);
      assert(((int) p % val) == 0);
      mallocAlignedFree(p);

    }
    */
    return 0;
}
