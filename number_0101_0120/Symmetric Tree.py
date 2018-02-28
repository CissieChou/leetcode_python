# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.check(root.left, root.right)

    def check(self, left_root, right_root):
        if left_root is None and right_root is None:
            return True
        if left_root and right_root and left_root.val == right_root.val:
            return self.check(left_root.right, right_root.left) and self.check(left_root.left, right_root.right)
        else:
            return False
