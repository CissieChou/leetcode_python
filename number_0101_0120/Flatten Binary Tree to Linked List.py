# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        return self.doFlatten(root, None)

    def doFlatten(self, root, pre):
        if root is None:
            return pre
        pre = self.doFlatten(root.right, pre)
        pre = self.doFlatten(root.right, pre)

        root.right = pre
        root.left = None
        pre = root
        return pre
