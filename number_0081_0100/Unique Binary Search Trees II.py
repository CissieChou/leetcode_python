# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from structure.TreeNode import TreeNode


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if n == 0:
            return []

        return self.backTrack(1, n)

    def backTrack(self, start, end):
        root_list = []
        if start > end:
            root_list.append(None)
            return root_list

        for index in range(start, end + 1):
            left_root_list = self.backTrack(start, index - 1)
            right_root_list = self.backTrack(index + 1, end)

            for left_root in left_root_list:
                for right_root in right_root_list:
                    new_root = TreeNode(index)
                    new_root.left = left_root
                    new_root.right = right_root
                    root_list.append(new_root)

        return root_list
