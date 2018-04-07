# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        results = []
        left = 1
        right = 2
        temp_sum = left + right

        mid = tsum / 2
        while left <= mid and right < tsum:
            if temp_sum < tsum:
                right += 1
                temp_sum += right
            elif temp_sum > tsum:
                temp_sum -= left
                left += 1
            else:
                result = list(range(left, right+1))
                results.append(result)

                temp_sum -= left
                left += 1
                right += 1
                temp_sum += right

        return results
