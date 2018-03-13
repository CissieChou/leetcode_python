# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from structure.ListNode import ListNode


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return

        pre = head
        tail = head
        while pre and pre.next and pre.next.next:
            pre = pre.next.next
            tail = tail.next

        print pre.val
        print tail.val
        right = self.reverseList(tail)
        left = head

        while left and right:
            left_next = left.next
            right_next = right.next
            left.next = right
            right.next = left_next
            left = left_next
            right = right_next

    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        tail = head
        pre = tail.next
        tail.next = None
        while pre:
            temp = pre.next
            pre.next = tail
            tail = pre
            pre = temp

        return tail

if __name__ == '__main__':
    listNode1 = ListNode(1)
    listNode2 = ListNode(2)
    listNode3 = ListNode(3)
    listNode4 = ListNode(4)

    listNode1.next = listNode2
    listNode2.next = listNode3
    listNode3.next = listNode4
    solution = Solution()
    solution.reorderList(listNode1)

    cur = listNode1
    while cur:
        print cur.val
        cur = cur.next