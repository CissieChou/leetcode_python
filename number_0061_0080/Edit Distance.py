class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        dp = []
        for i in range(len(word1) + 1):
            single_row = [0] * (len(word2) + 1)
            single_row[0] = i
            dp.append(single_row)

        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i, ch1 in enumerate(word1, 1):
            for j, ch2 in enumerate(word2, 1):
                if ch1 == ch2:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

        return dp[len(word1)][len(word2)]

