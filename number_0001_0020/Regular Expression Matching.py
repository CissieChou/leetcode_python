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


if __name__ == '__main__':
    s = "aa"
    p = "a*"
    # solution = Solution()
    # print solution.isMatch(s, p)
    print False or True and True

