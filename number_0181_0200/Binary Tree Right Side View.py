# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        level_result = dict()
        max_depth = -1

        stack = [(0, root)]
        while len(stack) > 0:
            depth, node = stack.pop()

            if node:
                max_depth = max(max_depth, depth)

                level_result.setdefault(depth, node.val)

                stack.append((depth+1, node.left))
                stack.append((depth+1, node.right))

        return [level_result[depth] for depth in range(max_depth+1)]
