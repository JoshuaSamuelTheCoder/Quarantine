/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){

    struct ListNode* c1 = l1;
    struct ListNode* c2 = l2;


    int carry = 0;
    int v1 = 0;
    int v2 = 0;
    int sw = 0;

    while(c1 != NULL && c2 != NULL) {
        v1 = c1->val;
        v2 = c2->val;

        int total = v1 + v2 + carry;
        carry = 0;
        if(total >= 10) {
            carry = floor(total / 10);
            total -= 10;
        }

        c1->val = total;
        c1 = c1->next;
        c2 = c2->next;
    }

    if(c2 != NULL) {
        c1 = l1;
        c2 = l2;
        while(c1 != NULL) {
            c2->val = c1->val;
            c1 = c1->next;
            c2 = c2->next;
        }
        if(carry > 0) {

            if(c2 != NULL) {
                printf("kill me");
                c2->val += carry;
                while(c2->val >= 10) {

                    carry = floor(c2->val  / 10);
                    c2->val -= 10;
                    if(c2->next == NULL) {
                        c2 = l2;
                        while(c2->next != NULL) {
                            c2 = c2->next;
                        }
                        c2->next = l1;
                        l1 = l1->next;
                        c2->next->val = carry;
                        carry = 0;
                        c2 = c2->next;
                        c2->next = NULL;
                    } else {
                        c2->next->val += carry;
                        c2 = c2->next;
                    }
                }


            } else {

                c2 = l2;
                while(c2->next != NULL) {
                    c2 = c2->next;
                }
                if(c2->val >= 10) {
                    c2->val -=10;
                }

                c2->next = l1;
                c2->next->val = carry;
                c2->next->next = NULL;
            }
        }

        return l2;
    }

    if (carry > 0) {
        if(c1 != NULL) {
                printf("kill me");
                c1->val += carry;
                while(c1->val >= 10) {

                    carry = floor(c1->val  / 10);
                    c1->val -= 10;
                    if(c1->next == NULL) {
                        c1 = l1;
                        while(c1->next != NULL) {
                            c1 = c1->next;
                        }
                        c1->next = l2;
                        l2 = l1->next;
                        c1->next->val = carry;
                        carry = 0;
                        c1 = c1->next;
                        c1->next = NULL;
                    } else {
                        c1->next->val += carry;
                        c1 = c1->next;
                    }
                }


            } else {

                c1 = l1;
                while(c1->next != NULL) {
                    c1 = c1->next;
                }
                if(c1->val >=10) {
                    c1->val -=10;
                }

                c1->next = l2;
                c1->next->val = carry;
                c1->next->next = NULL;
            }


    }
    return l1;




}
