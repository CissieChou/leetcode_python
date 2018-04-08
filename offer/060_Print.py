# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        results = []
        if pRoot is None:
            return results
        queue = [pRoot]

        while len(queue) > 0:
            results.append([node.val for node in queue])

            temp = []
            while len(queue) > 0:
                node = queue.pop(0)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp

        return results

