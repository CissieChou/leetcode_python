class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        cur_sum = nums[0]
        result = nums[0]
        for num in nums[1:]:
            if cur_sum <= 0:
                cur_sum = num
            else:
                cur_sum += num

            if cur_sum > result:
                result = cur_sum

        return result