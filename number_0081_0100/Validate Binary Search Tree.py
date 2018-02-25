# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        cur_node = root
        pre_val = - (1 << 31) - 1
        while len(stack) > 0 or cur_node:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                if cur_node.val < pre_val:
                    return False
                else:
                    pre_val = cur_node.val
                cur_node = cur_node.right

        return True



    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        min_val = -(1 << 31) - 1
        max_val = 1 << 31
        return self.check(root, min_val, max_val)

    def check(self, root, min_val, max_val):
        if root is None:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False

        return self.check(root.left, min_val, root.val) and self.check(root.right, root.val, max_val)