# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.backTrack(root, [])

        return self.result

    def backTrack(self, root, path_strs):
        if root is None:
            return

        if root.left is None and root.right is None:
            self.result += int("".join(path_strs) + str(root.val))
            return

        self.backTrack(root.left, path_strs + [str(root.val)])
        self.backTrack(root.right, path_strs + [str(root.val)])