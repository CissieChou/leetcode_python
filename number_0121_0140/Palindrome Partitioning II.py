class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = []
        for index in range(len(s)):
            dp.append([False] * len(s))

        result = [0] * len(s)

        for i in range(len(s)):
            cur_min = i
            for j in range(i+1):
                if s[i] == s[j] and (j + 1 > i - 1 or dp[i-1][j+1]):
                    dp[i][j] = True
                    cur_min = 0 if j == 0 else min(cur_min, result[j-1] + 1)

            result[i] = cur_min
        return result[len(s) - 1]
