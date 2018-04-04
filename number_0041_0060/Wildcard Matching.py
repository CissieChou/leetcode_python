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
                    if p[j] == "?":
                        ans = (i <= len(s) - 1) and dp(i+1, j+1)
                    elif p[j] == "*":
                        ans = dp(i, j+1) or (i <= len(s) - 1 and dp(i+1, j))
                    else:
                        ans = (i <= len(s) - 1) and dp(i+1, j+1) and s[i] == p[j]

                momo[(i, j)] = ans

            return momo[(i, j)]

        return dp(0, 0)
