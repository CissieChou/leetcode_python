# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        left = self.getFirstIndex(data, k)
        right = self.getLastIndex(data, k)

        if left == -1 or right == -1:
            return 0
        else:
            return right - left + 1

    def getFirstIndex(self, data, k):
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = left + (right - left)/2

            if data[mid] >= k:
                right = mid - 1
            else:
                left = mid + 1

        if left == len(data) or not data[left] == k:
            return -1
        else:
            return left


    def getLastIndex(self, data, k):
        left = 0
        right = len(data) - 1

        while left <= right:
            mid = left + (right - left)/2

            if data[mid] > k:
                right = mid - 1
            else:
                left = mid + 1

        if right == -1 or not data[right] == k:
            return -1
        else:
            return right