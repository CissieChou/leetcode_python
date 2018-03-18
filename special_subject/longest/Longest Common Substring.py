class Solution(object):
    def LongestCommonSubstring(self, s1, s2):
        """
        :type s: str
        :rtype: int
        """
        length1 = len(s1) + 1
        length2 = len(s2) + 1
        dp = [[0] * length1 for _ in range(length2)]

        for i in range(1, length2):
            for j in range(1, length1):
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0

        return dp[length2-1][length1-1]
