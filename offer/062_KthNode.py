# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    count = 0
    result = None
    def KthNode(self, pRoot, k):
        # write code here
        self.inOder(pRoot, k)
        return self.result

    def inOder(self,pRoot, k):
        if self.result is not None or pRoot is None:
            return
        self.KthNode(pRoot.left, k)
        self.count += 1
        if k == self.count:
            self.result = pRoot
            return
        self.KthNode(pRoot.right, k)
