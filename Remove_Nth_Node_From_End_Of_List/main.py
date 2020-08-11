"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.

Follow up:

Could you do this in one pass? Yes
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        ptr = head #this pointer will only start n timesteps after fast_ptr
        fast_ptr = head
        i = 0

        #1->2->3->4->5 n=2

        while fast_ptr != None:
            if i > n:
                ptr = ptr.next
            fast_ptr = fast_ptr.next
            i += 1

        if i > n and ptr.next is not None:
            ptr.next = ptr.next.next
        else:
            head = head.next

        return head
