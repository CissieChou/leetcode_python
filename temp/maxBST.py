# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MaxSubtree:
    def getNode(self, root):
        if root.left:
            lnode, lcount, lMaxNum, lMinNum = self.getNode(root.left)
        else:
            lnode, lcount, lMaxNum, lMinNum = None, 0, 0, 0

        if root.right:
            rnode, rcount, rMaxNum, rMinNum = self.getNode(root.right)
        else:
            rnode, rcount, rMaxNum, rMinNum = None, 0, 0, 0

        if lMaxNum < root.val and root.val < rMinNum and lnode == root.left and rnode == root.right:
            return root, lcount + rcount + 1, rMaxNum, lMinNum
        else:
            if lcount == 0 and rcount == 0:
                return root, 1, root.val, root.val
            if lcount > rcount:
                if lMaxNum < root.val and lnode == root.left and rcount == 0:
                    return root, lcount + 1, root.val, lMinNum
                else:
                    return lnode, lcount, lMaxNum, lMinNum
            else:
                if root.val < rMinNum and rnode == root.right and lcount == 0:
                    return root, rcount + 1, rMaxNum, root.val
                else:
                    return rnode, rcount, rMaxNum, rMinNum

    def getMax(self, root):
        # write code here
        node, count, maxNum, minNum = self.getNode(root)
        return node
