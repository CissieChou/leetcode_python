class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)/2
            pre_num = (-1<< 32 if mid == 0 else nums[mid-1])
            after_num = (-1<<32 if mid == len(nums) - 1 else nums[mid+1])
            if pre_num < nums[mid] > after_num:
                return mid
            elif pre_num > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

