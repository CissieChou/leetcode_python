# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from structure.ListNode import ListNode

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if not head:
            return head
        small_new_header = ListNode(-1)
        small_node = small_new_header
        big_new_header = ListNode(-1)
        big_node = big_new_header

        cur_node = head
        while cur_node is not None:
            if cur_node.val < x:
                small_node.next = cur_node
                small_node = cur_node
            else:
                big_node.next = cur_node
                big_node = cur_node

            cur_node = cur_node.next

        big_node.next = None
        small_node.next = big_new_header.next

        return small_new_header.next
