# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from structure.ListNode import ListNode

from structure.ListNode import ListNode

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        new_head = ListNode(-1)
        pre_val = head.val - 1
        result_node = new_head

        cur_node = head
        while cur_node is not None:
            if (cur_node.next is None or not cur_node.val == cur_node.next.val) and not cur_node.val == pre_val:
                result_node.next = cur_node
                result_node = cur_node

            pre_val = cur_node.val
            cur_node = cur_node.next

        result_node.next = None
        return new_head.next
