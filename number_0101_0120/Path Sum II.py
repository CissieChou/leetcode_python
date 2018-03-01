# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        results = []
        self.backTrack(root,results, [], 0, sum)
        return results

    def backTrack(self, root, results, single_result, cur_sum ,sum):
        if root is None:
            return
        cur_sum = cur_sum + root.val
        if root.left is None and root.right is None:
            if cur_sum == sum:
                results.append(single_result + [root.val])
            return
        self.backTrack(root.left, results, single_result + [root.val], cur_sum, sum)
        self.backTrack(root.right, results, single_result + [root.val], cur_sum, sum)
