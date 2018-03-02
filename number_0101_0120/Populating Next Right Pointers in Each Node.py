# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        pre = root

        while pre:
            cur = pre
            while pre and pre.left:
                pre.left.next = pre.right
                if pre.next:
                    pre.right.next = pre.next.left

                pre = pre.next

            pre = cur.left

        return root


