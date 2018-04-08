# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        stack1 = [pRoot]
        stack2 = []
        results = []
        while len(stack1) > 0 or len(stack2) > 0:
            if len(stack1) > 0:
                results.append([])
                while len(stack1) > 0:
                    node = stack1.pop()
                    results[-1].append(node.val)
                    if node.left:
                        stack2.append(node.left)
                    if node.right:
                        stack2.append(node.right)
            if len(stack2) > 0:
                results.append([])
                while len(stack2) > 0:
                    node = stack2.pop()
                    results[-1].append(node.val)
                    if node.right:
                        stack1.append(node.right)
                    if node.left:
                        stack1.append(node.left)
        return results


