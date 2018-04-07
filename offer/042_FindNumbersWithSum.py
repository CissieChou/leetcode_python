# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) <= 0:
            return []
        left = 0
        right = len(array) - 1
        cur_sum = array[left] + array[right]
        result = []
        while left < right:
            if cur_sum < tsum:
                left += 1
                cur_sum = array[left] + array[right]
            elif cur_sum > tsum:
                right -= 1
                cur_sum = array[left] + array[right]
            else:
                if not result:
                    result = [array[left], array[right]]
                else:
                    if array[left] * array[right] < result[0] * result[1]:
                        result = (array[left], array[right])

                left +=1
                right -= 1
        return result

