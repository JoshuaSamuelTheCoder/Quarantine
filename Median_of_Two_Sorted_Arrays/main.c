double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){

    int n = nums1Size + nums2Size;
    int *arr = malloc(sizeof(float)*(n));

    int one_pointer = 0;
    int two_pointer = 0;
    for(int i = 0; i < n; i++) {
       if(two_pointer == nums2Size || (one_pointer < nums1Size && nums1[one_pointer] <= nums2[two_pointer])) {
           arr[i] = nums1[one_pointer];
           one_pointer++;
       } else {
           arr[i] = nums2[two_pointer];
           two_pointer++;
       }
       //printf("%d,", arr[i]);
    }

    if(n % 2 == 1) {
        return arr[n/2];
    } else {
        printf("%f", (float)((arr[n/2-1] + arr[n/2])/2.0));
        return (float)((arr[n/2-1] + arr[n/2])/2.0);
    }
}
