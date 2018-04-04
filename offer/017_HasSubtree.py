# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 is None or pRoot1 is None:
            return False

        return self.doCheckHasSubtree(pRoot1, pRoot2)

    def doCheckHasSubtree(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        elif pRoot1 is None:
            return False

        flag = False
        if pRoot1.val == pRoot2.val:
            flag = self.doCheckHasSubtree(pRoot1.left, pRoot2.left) and self.doCheckHasSubtree(pRoot1.right, pRoot2.right)
        if not flag:
            flag = self.doCheckHasSubtree(pRoot1.left, pRoot2)
        if not flag:
            flag = self.doCheckHasSubtree(pRoot1.right, pRoot2)
        return flag