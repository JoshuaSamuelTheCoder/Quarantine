"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        rtn_lst = ListNode()
        node = rtn_lst
        continue_ = True
        while continue_:
            continue_ = False
            minIndex, minVal = None, float("inf")
            for i,l in enumerate(lists):
                if l is not None:
                    continue_ = True
                    val = l.val
                    if val < minVal:
                        minIndex = i
                        minVal = val
            if continue_:
                val = lists[minIndex]
                node.next = val
                lists[minIndex] = val.next
                node = node.next

                if val.next is None:
                    if minIndex == len(lists) - 1:
                        lists.pop()
                    else:
                        lists[minIndex] = lists.pop()
                val.next = None

        return rtn_lst.next
