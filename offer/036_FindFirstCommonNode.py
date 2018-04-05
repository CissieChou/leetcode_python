# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return None

        length1 = 0
        length2 = 0
        cur = pHead1
        while cur:
            cur = cur.next
            length1 += 1

        cur = pHead2
        while cur:
            cur = cur.next
            length2 += 1

        cur1 = pHead1
        cur2 = pHead2
        if length1 > length2:
            dif = length1 - length2
            while dif > 0:
                cur1 = cur1.next
                dif -= 1
        else:
            dif = length2 - length1
            while dif > 0:
                cur2 = cur2.next
                dif -= 1

        while cur1 and cur2:
            if cur1 == cur2:
                return cur1
            else:
                cur1 = cur1.next
                cur2 = cur2.next

        return None