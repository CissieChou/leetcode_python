class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n or n < 1:
            return []
        results = []
        self.backTrack(results, [], n, k, 1)
        return results

    def backTrack(self, results, single_result, n, k, start):
        if len(single_result) == k:
            results.append(single_result)
            return
        if len(single_result) + n - start + 1 < k:
            return
        for index in range(start, n + 1):
            self.backTrack(results, single_result + [index], n, k, index + 1)
