class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        left = - 1
        for right, num in enumerate(nums):
            if num == val:
                continue
            else:
                left += 1
                nums[left] = num

        return left + 1