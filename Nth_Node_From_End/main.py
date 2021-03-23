"""
Problem:
Given a linked list, return nth element from the tail of a linked list.
Example 0 -> 22-> 5-> 20-> 1-> 23-> 9-> 10-> NULL
Input: N=2
Output: 9
"""

class Node:
    def __init__(self, new_data, next=None):
        self.data = new_data
        self.next = next

def nth(list, n):
    slow, fast = list, list
    i = 0
    while(i < n):
        i += 1
        fast = fast.next
    while(fast is not None):
        slow = slow.next
        fast = fast.next

    return slow.data

if __name__ == "__main__":

    test_node = Node(0, Node(22, Node(5, Node(20, Node(1, Node(23, Node(9, Node(10))))))))
    print(nth(test_node, 2))
