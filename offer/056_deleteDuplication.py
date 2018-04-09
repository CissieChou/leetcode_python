# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from structure.ListNode import ListNode

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        next = pHead.next
        if pHead.val == next.val:
            while next and pHead.val == next.val:
                next = next.next
            return self.deleteDuplication(next)
        else:
            pHead.next = self.deleteDuplication(next)

        return pHead