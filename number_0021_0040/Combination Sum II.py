class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if len(candidates) == 0:
            return []
        candidates.sort()
        if candidates[0] > target:
            return []

        results = []
        print (candidates)
        self.backtrack(candidates, target, [], 0, results, 0)
        return results

    def backtrack(self, candidates, target, single_result, cur_sum, results, start):
        if cur_sum == target:
            results.append(single_result)
            return
        elif cur_sum > target or start == len(candidates):
            return

        for index, num in enumerate(candidates[start:]):

            if index > 0 and candidates[start + index] == candidates[start + index - 1]:
                continue

            self.backtrack(candidates, target, single_result + [num], cur_sum + num, results, start + index + 1)

if __name__ == '__main__':
    solution = Solution()
    nums = [10, 1, 2, 7, 6, 1, 5]

    print (solution.combinationSum2(nums, 8))