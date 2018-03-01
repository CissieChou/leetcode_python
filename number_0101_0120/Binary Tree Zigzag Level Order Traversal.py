# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        results = []

        odd_level_nodes = [root]
        even_level_nodes = []

        while len(even_level_nodes) > 0 or len(odd_level_nodes) > 0:
            if len(odd_level_nodes) > 0:
                results.append([])
                while len(odd_level_nodes) > 0:
                    node = odd_level_nodes.pop()
                    results[-1].append(node.val)
                    if node.left:
                        even_level_nodes.append(node.right)
                    if node.right:
                        even_level_nodes.append(node.left)

            if len(even_level_nodes) > 0:
                results.append([])
                while len(even_level_nodes) > 0:
                    node = even_level_nodes.pop()
                    results[-1].append(node.val)
                    if node.right:
                        odd_level_nodes.append(node.right)
                    if node.left:
                        odd_level_nodes.append(node.left)
        return results


if __name__ == '__main__':
    x = [1,2,3]
    print(x.pop(0))