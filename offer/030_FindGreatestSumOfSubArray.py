# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) ==0:
            return 0
        dp = [0] * len(array)
        for index, num in enumerate(array):
            if index == 0:
                dp[index] = num
            else:
                if dp[index - 1] > 0:
                    dp[index] = dp[index-1] + num
                else:
                    dp[index] = num
        return max(dp)
