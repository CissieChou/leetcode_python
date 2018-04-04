# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        if pRootOfTree.left is None and pRootOfTree.right is None:
            return pRootOfTree

        left_head = self.Convert(pRootOfTree.left)

        cur = left_head
        while cur and cur.right:
            cur = cur.right
        if cur:
            cur.right = pRootOfTree
            # pRootOfTree.left = cur

        right = self.Convert(pRootOfTree.right)

        if right:
            right.left = pRootOfTree
            # pRootOfTree.right = right

        if left_head:
            return left_head
        else:
            return pRootOfTree