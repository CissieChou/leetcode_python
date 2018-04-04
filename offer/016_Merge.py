# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from structure import ListNode
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1
        dummy = ListNode(-1)
        cur = dummy
        while pHead1 and pHead2.val:
            if pHead1.val > pHead2:
                cur.next = ListNode(pHead1.val)
                pHead1 = pHead1.next
            else:
                cur.next = ListNode(pHead2.val)
                pHead2 = pHead2.next
            cur = cur.next
        if pHead1:
            cur.next = pHead1
        else:
            cur.next = pHead2
        return dummy.next

