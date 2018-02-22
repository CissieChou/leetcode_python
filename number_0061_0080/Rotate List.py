from structure import ListNode


class Solution(object):
    '''
    Given 1->2->3->4->5->NULL and k = 2,

    return 4->5->1->2->3->NULL.
    '''
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head

        pre = head
        count = 0
        while pre:
            pre = pre.next
            count += 1

        k = k%count
        if k == 0:
            return head

        pre = head
        tail = head
        while k > 0:
            pre = pre.next
            k -= 1

        while pre and pre.next:
            pre = pre.next
            tail = tail.next

        new_head = tail.next
        tail.next = None
        pre.next = head

        return new_head