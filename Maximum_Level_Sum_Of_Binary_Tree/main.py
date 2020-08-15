"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.



Example 1:

Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.



Note:

    The number of nodes in the given tree is between 1 and 10^4.
    -10^5 <= node.val <= 10^5

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        levels_sum = []
        job_lst = [root]

        while job_lst:

            levels_sum.append(sum(j.val for j in job_lst))
            new_job_lst = []

            for level in job_lst:
                if level.left:
                    new_job_lst.append(level.left)
                if level.right:
                    new_job_lst.append(level.right)
            job_lst = new_job_lst

        return levels_sum.index(max(levels_sum)) + 1
