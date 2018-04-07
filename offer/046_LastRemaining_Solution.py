# -*- coding:utf-8 -*-
class Solution:
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0 or m == 0:
            return -1
        if n == 1:
            return 0
        nodes = []
        for index in range(n):
            nodes.append(Solution.ListNode(index))

        for index in range(n):
            if index == 0:
                nodes[-1].next = nodes[0]
            else:
                nodes[index-1].next = nodes[index]

        cur = nodes[0]
        for i in range(n-1):
            for j in range(m-2):
                cur = cur.next
            cur.next = cur.next.next
            cur = cur.next

        return cur.val