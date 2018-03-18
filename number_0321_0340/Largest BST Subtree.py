# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root

        node, count, max_val, min_val = self.findlargestBSTSubtree(root)
        return node

    def findlargestBSTSubtree(self, root):
        if root is None:
            return None, 0, (1 << 31) - 1, -1 << 31

        left_node, left_count, left_max_val, left_min_val = self.findlargestBSTSubtree(root.left)
        right_node, right_count, right_max_val, right_min_val = self.findlargestBSTSubtree(root.right)

        min_val = min(left_min_val, root.val)
        max_val = max(right_max_val, root.val)

        if root.left == left_node and root.right == right_node \
                and left_max_val < root.val < right_min_val:
            count = left_count + right_count + 1
            return root, count, max_val, min_val

        if left_count > right_count:
            return left_node, left_count, max_val, min_val
        else:
            return right_node, right_count, max_val, min_val




