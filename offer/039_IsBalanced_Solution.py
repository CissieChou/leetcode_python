# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def IsBalanced_Solution(self, pRoot):
        # write code here
        return not self.doIsBalanced(pRoot) == -1

    def doIsBalanced(self, pRoot):
        if pRoot is None:
            return 0

        left = self.doIsBalanced(pRoot.left)
        if left == -1:
            return -1

        right = self.doIsBalanced(pRoot.right)
        if right == -1:
            return -1

        dif = abs(left - right)
        if dif > 1:
            return -1
        else:
            return max(left, right) + 1
