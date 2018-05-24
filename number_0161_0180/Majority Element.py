class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 1
        temp = nums[0]
        for num in nums[1:]:
            if count == 0:
                temp = num
                count = 1
            elif temp == num:
                count += 1
            else:
                count -= 1

        return temp
