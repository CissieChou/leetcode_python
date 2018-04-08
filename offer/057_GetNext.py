# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        result = None
        if pNode.right:
            cur = pNode.right
            while cur and cur.left:
                cur = cur.left
            result = cur
        elif pNode.next is not None:
            cur = pNode
            parent = pNode.next

            while parent and parent.right == cur:
                cur = parent
                parent = parent.next
            result = parent

        return result