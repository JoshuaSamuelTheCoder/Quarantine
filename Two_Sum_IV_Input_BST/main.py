"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True



Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def findTargetHelper(self, root, k):


        if root == None:
            return False
        elif k-root.val in self.seen:
            return True
        else:
            self.seen.add(root.val)

            not_used_left = self.findTargetHelper(root.left, k)
            not_used_right = self.findTargetHelper(root.right, k)

            return not_used_left or not_used_right


    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.seen = set()
        return self.findTargetHelper(root, k)

        
