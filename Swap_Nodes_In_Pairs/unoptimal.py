# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        flag = False
        ptr_left = head
        ptr_iter = head

        while ptr_iter != None:
            if not flag:
                ptr_left = ptr_iter
            else:
                ptr_left.val, ptr_iter.val = ptr_iter.val, ptr_left.val
            flag = not flag
            ptr_iter = ptr_iter.next

        return head
