# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        results = []
        even_level_nodes = [root]
        odd_level_nodes = []

        while len(even_level_nodes) > 0 or len(odd_level_nodes) > 0:
            if len(even_level_nodes) > 0:
                pass


        return results