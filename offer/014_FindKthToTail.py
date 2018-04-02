# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None:
            return None
        pre = head
        tail = head

        while tail and k > 0:
            tail = tail.next
            k -= 1

        if k > 0:
            return None

        while tail:
            pre = pre.next
            tail = tail.next
        return pre
