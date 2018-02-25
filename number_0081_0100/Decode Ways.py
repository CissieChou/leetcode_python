class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == "0":
            return 0
        elif len(s) == 1:
            return 1
        elif len(s) == 2:
            num = int(s)
            if num > 26:
                if s[-1] == "0":
                    return 0
                else:
                    return 1
            elif num == 10 or num == 20:
                return 1
            else:
                return 2
        else:
            if int(s[:2]) > 26:
                return self.numDecodings(s[1:])
            elif s[:2] == "10" or s[:2] == "20":
                return self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])


if __name__ == '__main__':
    s = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
    solution = Solution()
    print(solution.numDecodings(s))
    print("27" > "028")