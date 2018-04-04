# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        results = []
        self.dfs(root, expectNumber, [], results)
        return results

    def dfs(self, root, rest, single_result, results):
        if root is None:
            return
        if root.left is None and root.right is None:
            if rest == root.val:
                results.append(single_result + [root.val])
                return
        else:
            self.dfs(root.left, rest - root.val, single_result + [root.val], results)
            self.dfs(root.right, rest - root.val, single_result + [root.val], results)