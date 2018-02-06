class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        new_head = head.next
        next_start = head.next.next
        head.next.next = head
        head.next = self.swapPairs(next_start)
        return new_head
