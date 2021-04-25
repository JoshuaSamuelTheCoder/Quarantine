/*
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Examples:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
*/

/*
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
*/

#include <limits.h>
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){

    struct ListNode *t1 = l1;
    struct ListNode *t2 = l2;

    struct ListNode *head = NULL;
    struct ListNode *cur = NULL;

    while(t1 != NULL || t2 != NULL) {

        int v1 = INT_MAX;
        int v2 = INT_MAX;
        if(t1 != NULL) {
            v1 = t1->val;
        }
        if(t2 != NULL) {
            v2 = t2->val;
        }

        if(v1 <= v2) {
            if(head == NULL) {
                head = t1;
            } else {
                cur->next = t1;
            }
            t1 = t1->next;
        } else {
             if(head == NULL) {
                head = t2;
            } else {
                cur->next = t2;
            }
            t2 = t2->next;
        }
        if(cur == NULL) {
            cur = head;
        } else {
            cur = cur->next;
        }

    }
    return head;
}
