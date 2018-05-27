class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        second = 0

        for index in range(len(nums)):
            if index&1== 0:
                first = max(first + nums[index], second)
            else:
                second = max(second + nums[index], first)

        return max(first, second)