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

