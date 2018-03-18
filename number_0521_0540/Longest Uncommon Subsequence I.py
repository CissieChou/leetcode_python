class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1

        return max(len(a), len(b))


if __name__ == '__main__':
    a, b = "a", "bc"
    solution = Solution()
    print (solution.findLUSlength(a, b))