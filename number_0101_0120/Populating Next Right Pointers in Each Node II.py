# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

from structure.TreeNode import TreeNode


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        pre = root
        level = 0
        while pre and (pre.left or pre.right):
            print(level)
            cur = pre
            temp = None
            while pre:
                if pre.left:
                    if temp is not None:
                        temp.next = pre.left
                    if pre.right:
                        pre.left.next = pre.right
                        temp = pre.right
                    else:
                        temp = pre.left
                elif pre.right:
                    if temp is not None:
                        temp.next = pre.right
                    temp = pre.right

                pre = pre.next

            if cur.left:
                pre = cur.left
            else:
                pre = cur.right

            while pre.left is None and pre.right is None:
                pre = pre.next

            level += 1

    def connect_recursive(self, root):
        if root:
            return
        dummy = TreeNode(-1)
        pre = dummy
        cur = root
        while cur:
            if cur.left:
                pre.next = cur.left
                pre = cur.left
            if cur.right:
                pre.next = cur.right
                pre = cur.right
            cur = cur.next
        self.connect_recursive(dummy.next)

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node1.left = node2

    solution = Solution()
    solution.connect(node1)
