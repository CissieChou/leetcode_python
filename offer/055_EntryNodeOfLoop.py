# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here

        if pHead is None:
            return None
        slow = pHead
        fast = pHead

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                fast = pHead
                while not fast == slow:
                    fast = fast.next
                    slow = slow.next
                return slow

        return None




