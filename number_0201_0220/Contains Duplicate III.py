import math
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i, num in enumerate(nums):
            end = max(0, i - k)
            for j in range(end, i):
                if abs(num - nums[j]) <= t:
                    return True
        return False
