class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        self.dfs(results,[],k,n,1,0)
        return results

    def dfs(self, results, single_result, k, n, start, cur_sum):
        if len(single_result) == k and cur_sum == n:
            results.append(single_result)
            return

        if len(single_result) == k or cur_sum > n:
            return

        for num in range(start, 10):
            self.dfs(results, single_result + [num], k,n, num + 1, cur_sum + num)
