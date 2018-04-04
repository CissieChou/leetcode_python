# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None

        self.NewNode(pHead)
        self.linkRandom(pHead)
        return self.split(pHead)

    def NewNode(self, pHead):
        cur = pHead
        while cur:
            new_node = RandomListNode(cur.label)
            new_node.next = cur.next
            new_node.random = cur.random
            cur.next = new_node
            cur = new_node.next

        return pHead

    def linkRandom(self, pHead):
        cur = pHead
        while cur:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next

    def split(self, pHead):
        cur = pHead
        result_head = pHead.next
        result_cur = pHead.next

        while cur:
            cur_next = result_cur.next
            cur.next = cur_next
            if cur_next is not None:
                result_cur.next = cur_next.next
            cur = cur.next
            result_cur = result_cur.next

        return result_head