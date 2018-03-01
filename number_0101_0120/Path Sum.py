# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    flag = False
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.backTrack(root, 0, sum)
        return self.flag

    def backTrack(self, root, cur_sum, sum):
        if root is None or self.flag:
            return
        cur_sum = cur_sum + root.val
        if root.left is None and root.right is None:
            if cur_sum == sum:
                self.flag = True
                return
        else:
            self.backTrack(root.left, cur_sum, sum)
            self.backTrack(root.right, cur_sum, sum)

