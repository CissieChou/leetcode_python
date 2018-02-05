from structure import ListNode

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        mock_head = ListNode(-1)
        mock_head.next = head

        pre = mock_head
        tail = mock_head
        while n:
            pre = pre.next
            n -= 1
        while pre and pre.next:
            pre = pre.next
            tail = tail.next

        tail.next = tail.next.next
        return mock_head.next
