# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    minResult = 1 << 31 - 1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.backTrack(root, 0)
        return self.minResult

    def backTrack(self,root,cur_depth):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            if cur_depth + 1 < self.minResult:
                self.minResult = cur_depth + 1
        else:
            self.backTrack(root.left, cur_depth + 1)
            self.backTrack(root.right, cur_depth + 1)