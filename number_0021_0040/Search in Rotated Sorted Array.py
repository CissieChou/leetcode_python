class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        result = -1

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + int((right - left) / 2)
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[0]:
                if nums[0] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid

        if nums[left] == target:
            result = left
        return result