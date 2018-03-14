class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = nums[0]
        max_r = r
        min_r = r
        for num in nums[1:]:
            if num < 0:
                max_r, min_r = min_r, max_r

            max_r = max(num, num * max_r)
            min_r = min(num, num * min_r)

            r = max(r, max_r)

        return r
