class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def common_rob(nums):
            first = 0
            second = 0
            for index, num in enumerate(nums):
                if index & 1 == 0:
                    second = max(second + num, first)
                else:
                    first = max(first + num, second)
            return max(first, second)

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(common_rob(nums[:-1]), common_rob(nums[1:]))