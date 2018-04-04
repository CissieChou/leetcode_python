# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0

        left = 0
        right = len(rotateArray) -1
        while left < right:
            mid = left + (right - left)/2

            if rotateArray[mid] < rotateArray[right]:
                right = mid
            elif rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            else:
                right -= 1

        return rotateArray[left]

