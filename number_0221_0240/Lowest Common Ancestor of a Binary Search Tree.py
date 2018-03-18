# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None
        left_val = min(q.val, p.val)
        right_val = max(q.val, p.val)

        while not left_val <= root.val <= right_val:
            if root.val > right_val:
                root = root.left
            else:
                root = root.right
                
        return root