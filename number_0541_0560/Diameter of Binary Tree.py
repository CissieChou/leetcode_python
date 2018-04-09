# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 1

        def depth(root):
            if root is None:
                return 0

            left = depth(root.left)
            right = depth(root.right)

            self.ans = max(self.ans, left + right + 1)
            return max(left, right) + 1

        depth(root)
        return ans - 1