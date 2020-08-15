# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def traverseTree(self, node, level):

        if node == None:
            return 0
        else:
            if level >= len(self.level_data):
                self.level_data.append(node.val)
            else:
                self.level_data[level] += node.val
            self.traverseTree(node.left, level+1)
            self.traverseTree(node.right, level+1)

    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.level_data = []


        self.traverseTree(root, 0)

        max_level = float("-inf")
        max_ind = 0
        for i,sum_level in enumerate(self.level_data):
            if sum_level > max_level:
                max_level = sum_level
                max_ind = i
        return max_ind+1
