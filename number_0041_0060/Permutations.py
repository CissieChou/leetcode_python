from __future__ import print_function
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        flags = [False] * len(nums)
        self.backtrack(results, [], flags, nums)
        return results

    def backtrack(self, results, single_result, flags, nums):
        if len(single_result) == len(nums):
            results.append(single_result)
            return

        for index, num in enumerate(nums):
            if flags[index]:
                continue
            flags[index] = True
            self.backtrack(results, single_result + [num], flags, nums)
            flags[index] = False


if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    print (solution.permute(nums))