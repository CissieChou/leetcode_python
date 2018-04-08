# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from structure.TreeNode import TreeNode

class Solution:
    def Serialize(self, root):
        # write code here
        if root is None:
            return "#"
        result = []
        self.preOrderSer(root, result)

        return ",".join(result)

    def preOrderSer(self, root, result):
        if root is None:
            result.append("#")
            return
        result.append(str(root.val))
        self.preOrderSer(root.left, result)
        self.preOrderSer(root.right, result)

    def Deserialize(self, s):
        # write code here
        items = s.split(",")
        print (items)
        if len(s) == 0:
            return None
        return self.preOrderDes(items)

    def preOrderDes(self, items):
        if len(items) == 0:
            return None
        item = items.pop(0)
        if item == "#":
            return None
        else:
            root = TreeNode(int(item))

            root.left = self.preOrderDes(items)
            root.right = self.preOrderDes(items)
            return root

if __name__ == '__main__':
    s = "1,2,4,#,#,#,3,5,#,#,6,#,#"
    solution = Solution()
    root = solution.Deserialize(s)
    def preOder(root):
        if root is None:
            return
        print (root.val)
        preOder(root.left)
        preOder(root.right)

    preOder(root)