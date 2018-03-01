# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from structure.TreeNode import TreeNode

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None

        root_val = postorder[-1]
        root_val_index = -1
        for index, val in enumerate(inorder):
            if val == root_val:
                root_val_index = index
                break

        root_node = TreeNode(root_val)
        root_node.left = self.buildTree(inorder[:root_val_index], postorder[:root_val_index])
        root_node.right = self.buildTree(inorder[root_val_index+1:], postorder[root_val_index:-1])
        return root_node
