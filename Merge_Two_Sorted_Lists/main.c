/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){

    if(l1 == NULL) {
        return l2;
    } else if(l2 == NULL) {
        return l1;
    }

    struct ListNode* l3;
    struct ListNode* p1 = l1;
    struct ListNode* p2 = l2;

    if(p1->val < p2->val) {
        l3 = p1;
        p1 = p1->next;
    } else {
        l3 = p2;
        p2 = p2->next;
    }
    struct ListNode* p3 = l3;

    while(p1 != NULL || p2 != NULL) {
        if (p1 == NULL) {
            p3->next = p2;
            p2 = p2->next;
            p3 = p3->next;
            continue;
        } else if(p2 == NULL) {
            p3->next = p1;
            p1 = p1->next;
            p3 = p3->next;
            continue;
        }

        if(p1->val < p2->val) {
            p3->next = p1;
            p1 = p1->next;
        } else {
            p3->next = p2;
            p2 = p2->next;
        }
        p3 = p3->next;
    }
    return l3;
}
