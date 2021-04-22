#include <stdio.h>
#include <stdlib.h>

 struct Node{

  int val;
  struct Node *next;

};

typedef struct Node Node;

Node* deleteNode(Node *head, int key) {
  Node *n = head;
  while (n->next != NULL) {
    if (n->next->val == key) {
      Node *last = n->next->next;
      n->next->next = NULL;
      Node *rtn_node = n->next;
      n->next = last;
      return rtn_node;
    }
    n = n->next;
  }
  return NULL;

}


int main() {
    Node *h = (Node*) malloc(sizeof(Node));
    h->val = 0;
    Node *n = h;
    for (int i = 1; i < 10; i++) {
      n->next = (Node*)malloc(sizeof(Node));
      n->next->val = i;
      n = n->next;
    }
    n = h;
    while(n != NULL) {
      printf("%d\n", n->val);
      n = n->next;
    }

    Node *d = deleteNode(h, 5);
    printf("Deleted Node: %d\n", d->val);

    n = h;
    while(n != NULL) {
      printf("%d\n", n->val);
      n = n->next;
    }

    return 0;
}
  
