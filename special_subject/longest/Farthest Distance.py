# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# find longest path in a tree
class Solution(object):

    result = 0
    def FarthestDistance(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.backTrack(root)
        return self.result

    def backTrack(self, root):
        if root is None:
            return 0

        left_height = self.backTrack(root.left)
        right_height = self.backTrack(root.right)
        temp_result = left_height + right_height + 1
        if temp_result > self.result:
            self.result = temp_result
        return max(left_height, right_height) + 1
