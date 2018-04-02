# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from structure import TreeNode
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        root_val = pre[0]
        root_index = 0
        for index, val in enumerate(tin):
            if root_val == val:
                root_index = index
                break
        root_node = TreeNode(root_val)
        root_node.left = self.reConstructBinaryTree(pre[1:1+root_index], tin[:root_index])
        root_node.right = self.reConstructBinaryTree(pre[1+root_index:], tin[root_index+1:])
        return root_node
