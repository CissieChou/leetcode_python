# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        pre_val = head.val
        cur_node = head.next
        result_node = head

        while cur_node is not None:

            if not cur_node.val == pre_val:
                pre_val = cur_node.val
                result_node.next = cur_node
                result_node = cur_node

            cur_node = cur_node.next

        result_node.next = None
        return head
