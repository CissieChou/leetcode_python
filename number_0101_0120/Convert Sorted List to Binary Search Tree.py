# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from structure.TreeNode import TreeNode
from structure.ListNode import ListNode


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        elif head.next is None:
            return TreeNode(head.val)

        total_count = 0

        cur_node = head
        while cur_node is not None:
            cur_node = cur_node.next
            total_count += 1

        mid_count = int(total_count/2)

        cur_node = head
        while mid_count > 1:
            cur_node = cur_node.next
            mid_count -= 1

        root_tree_node = TreeNode(cur_node.next.val)
        right_head = cur_node.next.next
        cur_node.next = None
        root_tree_node.left = self.sortedListToBST(head)
        root_tree_node.right = self.sortedListToBST(right_head)

        return root_tree_node
