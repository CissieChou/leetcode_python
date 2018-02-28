# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        pre = head
        tail = head.next
        pre.next = None

        while tail is not None:
            temp = tail.next
            tail.next = pre
            pre = tail
            tail = temp

        return pre