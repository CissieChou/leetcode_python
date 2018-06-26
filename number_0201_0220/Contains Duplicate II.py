class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_index = {}
        for index, num in enumerate(nums):
            if num in num_index:
                pre_index = num_index[num]
                if index - pre_index <= k:
                    return True
                else:
                    num_index[num] = index
            else:
                num_index[num] = index

        return False
    