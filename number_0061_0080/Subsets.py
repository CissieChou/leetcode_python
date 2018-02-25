class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        self.backTrack(results, [], nums, 0)
        return results

    def backTrack(self, results, single_result, nums, start):
        results.append(single_result)

        print(start, single_result)
        for index in range(start, len(nums)):
            self.backTrack(results, single_result + [nums[index]], nums, index + 1)

if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    print(solution.subsets(nums))
