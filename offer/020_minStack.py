# -*- coding:utf-8 -*-
class Solution:
    raw_stack = []
    min_stack = []

    def push(self, node):
        # write code here
        if len(self.raw_stack) == 0:
            self.raw_stack.append(node)
            self.min_stack.append(node)
        else:
            if node < self.min_stack[-1]:
                self.min_stack.append(node)
            else:
                self.min_stack.append(self.min_stack[-1])

            self.raw_stack.append(node)

    def pop(self):
        # write code here
        self.min_stack.pop()
        return self.raw_stack.pop()

    def top(self):
        # write code here
        return self.raw_stack[-1]

    def min(self):
        # write code here
        return self.min_stack[-1]