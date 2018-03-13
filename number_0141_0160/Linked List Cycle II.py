# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = head
        tail = head

        flag = False
        while pre and pre.next:
            pre = pre.next.next
            tail = tail.next
            if pre == tail:
                flag = True
                break

        if flag:
            tail = head
            while not tail == pre:
                tail = tail.next
                pre = pre.next

            return tail
        else:
            return None