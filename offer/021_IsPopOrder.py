# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        for push_item in pushV:
            stack.append(push_item)

            while stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)

        return len(stack) == 0