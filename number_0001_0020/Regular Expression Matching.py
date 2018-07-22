class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        momo = {}

        def dp(i, j):
            if (i, j) not in momo:
                if j == len(p):
                    ans = (i == len(s))
                else:
                    firstMatch = (i < len(s)) and (p[j] in {s[i], "."})

                    if j + 1 < len(p) and p[j+1] == "*":
                        ans = dp(i, j+2) or (firstMatch and dp(i+1,j))
                    else:
                        ans = dp(i+1,j+1) and firstMatch

                momo[(i, j)] = ans
            else:
                return momo[(i, j)]

        return dp(0, 0)

    def isMatch2(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) -1 , -1, -1):
                first_match = i < len(s) and p[j] in {s[i],"."}
                if j < len(p) - 1 and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]


if __name__ == '__main__':
    s = "aa"
    p = "a*"
    # solution = Solution()
    # print solution.isMatch(s, p)

