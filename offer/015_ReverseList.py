# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return pHead
        pre = pHead
        tail = pHead.next
        pre.next = None

        while tail:
            temp = tail.next
            tail.next = pre
            pre = tail
            tail = temp

        return pre

    def ReverseList2(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead

        next = pHead.next
        pHead.next = None
        new_head = self.ReverseList2(next)
        next.next = pHead
        return new_head


