# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from structure.TreeNode import TreeNode


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) /2

        root_node = TreeNode(nums[mid])

        root_node.left = self.sortedArrayToBST(nums[:mid])
        root_node.right = self.sortedArrayToBST(nums[mid+1:])
        return root_node