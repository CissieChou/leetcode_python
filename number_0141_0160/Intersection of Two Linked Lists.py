# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        count_a = 1
        count_b = 1

        cur = headA
        while cur:
            cur = cur.next
            count_a += 1

        cur = headB
        while cur:
            cur = cur.next
            count_b += 1

        cur_a = headA
        cur_b = headB
        if count_a > count_b:
            diff = count_a - count_b
            while diff > 0:
                cur_a = cur_a.next
                diff -= 1
        else:
            diff = count_b - count_a
            while diff > 0:
                cur_b = cur_b.next
                diff -= 1

        while not cur_a == cur_b and cur_a:
            cur_a = cur_a.next
            cur_b = cur_b.next

        return cur_a