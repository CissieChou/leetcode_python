# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from structure.ListNode import ListNode


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None or m == n:
            return head

        new_header = ListNode(-1)

        new_header.next = head
        left_node = new_header
        cur_node = new_header

        rest = m
        while rest > 0:
            left_node = cur_node
            cur_node = cur_node.next
            rest -= 1

        pre = cur_node
        tail = cur_node.next

        rest = n - m
        while rest > 0:
            temp = tail.next
            tail.next = pre
            pre = tail
            tail = temp
            rest -= 1

        left_node.next.next = tail
        left_node.next = pre
        return new_header.next