# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.checkIsSymmetrical(pRoot, pRoot)

    def checkIsSymmetrical(self, root1, roo2):
        if root1 is None:
            if roo2 is None:
                return True
            else:
                return False
        else:
            if roo2 is None:
                return False

            if root1.val == roo2.val:
                return self.checkIsSymmetrical(root1.left, roo2.right) and self.checkIsSymmetrical(root1.right, roo2.left)
            else:
                return False