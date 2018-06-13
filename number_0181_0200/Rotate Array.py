class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reserve(nums, 0, len(nums) - 1)
        self.reserve(nums, 0, k - 1)
        self.reserve(nums, k, len(nums) - 1)

    def reserve(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1