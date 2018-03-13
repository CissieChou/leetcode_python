class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        for num in nums:
            temp ^= num

        return temp
