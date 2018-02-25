class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        left = 1
        count = 1
        MAX_COUNT = 2
        cur_num = nums[0]
        for index in range(1, len(nums)):
            if nums[index] == cur_num:
                if count < MAX_COUNT:
                    nums[left] = nums[index]
                    left += 1
                    count += 1
                else:
                    continue
            else:
                nums[left] = nums[index]
                cur_num = nums[index]
                left += 1
                count = 1

        return left - 1

