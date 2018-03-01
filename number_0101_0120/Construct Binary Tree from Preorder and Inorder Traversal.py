# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from structure.TreeNode import TreeNode

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None

        root_val = preorder[0]

        root_val_index = -1
        for index, val in enumerate(inorder):
            if val == root_val:
                root_val_index = index
                break

        root_node = TreeNode(root_val)

        root_node.left = self.buildTree(preorder[1:1 + root_val_index], inorder[:root_val_index])
        root_node.right = self.buildTree(preorder[1 + root_val_index:], inorder[root_val_index+1:])
        return root_node


if __name__ == '__main__':
    x = [1,2]
    print(x[1:1])