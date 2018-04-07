# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        result = [1] * len(A)

        for index in range(1, len(A)):
            result[index] *= A[index - 1]
        temp = 1

        for index in range(len(A)- 2, -1,-1):
            temp *= A[index+1]
            result[index] *= temp
        return result