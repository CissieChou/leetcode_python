# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root is None:
            return
        queue = [root]
        pre_level_count = len(queue)
        results = []
        while len(queue) > 0:
            while pre_level_count > 0:
                node = queue.pop(0)
                results.append(node.val)
                pre_level_count -= 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            pre_level_count = len(queue)

        return results