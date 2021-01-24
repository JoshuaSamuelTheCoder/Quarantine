"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 """

 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def arrayToBST(self, nums, node):
        if len(nums) == 0:
            return
        if node is not None:
            length = len(nums)//2
            split_l = nums[0:length]
            split_r = nums[length+1:]

            if length > 0:
                node.left = TreeNode(split_l[len(split_l)//2])
                self.arrayToBST(split_l,node.left)
            if len(split_r) > 0:
                node.right = TreeNode(split_r[len(split_r)//2])
                self.arrayToBST(split_r,node.right)


    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        length = len(nums)//2
        head = TreeNode(nums[length])
        self.arrayToBST(nums, head)
        return head
