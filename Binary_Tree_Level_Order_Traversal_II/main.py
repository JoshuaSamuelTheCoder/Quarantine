"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        q = deque()
        stk = deque()
        if root is not None:
            q.append([root])
            stk.append([root.val])

        while len(q) > 0:
            item = q.popleft()

            new_lst = []
            stk_lst = []
            for i in item:
                if i.left:
                    new_lst.append(i.left)
                    stk_lst.append(i.left.val)
                if i.right:
                    new_lst.append(i.right)
                    stk_lst.append(i.right.val)
            if new_lst:
                q.append(new_lst)
                stk.append(stk_lst)

        rtn_lst = []
        while len(stk) > 0:
            rtn_lst.append(stk.pop())
        return rtn_lst
