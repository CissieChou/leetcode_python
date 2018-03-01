# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        results = []
        level_nodes = [root]

        while len(level_nodes) > 0:
            results.append([])
            next_level_nodes = []
            for node in level_nodes:
                results[-1].append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

            level_nodes = next_level_nodes

        return results[::-1]
