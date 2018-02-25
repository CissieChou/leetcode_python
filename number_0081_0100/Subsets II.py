class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        results = []
        nums.sort()
        self.backTrack(results,[], nums, 0)
        return results

    def backTrack(self, results, single_result, nums, start):
        results.append(single_result)

        for index in range(start, len(nums)):
            if index > start and nums[index] == nums[index - 1]:
                continue

            self.backTrack(results, single_result + [nums[index]], nums, index + 1)
