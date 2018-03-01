# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return None

        results = []
        level_result = [root]

        while len(level_result) > 0:
            results.append([node.val for node in level_result])
            next_level_result = []
            for node in level_result:
                if node.left:
                    next_level_result.append(node.left)

                if node.right:
                    next_level_result.append(node.right)
            level_result = next_level_result

        return results
