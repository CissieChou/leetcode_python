from __future__ import print_function
from __future__ import absolute_import
from structure.ListNode import ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0

        head_node = None
        cur_node = None
        while(l1 is not None or l2 is not None or carry > 0):
            if l1 is None:
                num1 = 0
            else:
                num1 = l1.val
                l1 = l1.next

            if l2 is None:
                num2 = 0
            else:
                num2 = l2.val
                l2 = l2.next

            new_num = num1 + num2 + carry
            if new_num >= 10:
                new_num %= 10
                carry = 1
            else:
                carry = 0

            new_node = ListNode(new_num)

            if head_node is None:
                head_node = new_node
                cur_node = head_node
            else:
                cur_node.next = new_node
                cur_node = new_node

        return head_node

if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(5)
    l2 = ListNode(5)

    node = solution.addTwoNumbers(l1,l2)
    while(node):
        print (node.val)
        node = node.next