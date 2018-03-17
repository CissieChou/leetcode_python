class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = 1 << 31
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack.pop() == self.min:
            self.min = self.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

