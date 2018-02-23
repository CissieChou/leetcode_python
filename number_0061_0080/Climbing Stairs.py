class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        if n == 2:
            return 2

        pre_1 = 1
        pre_2 = 2

        for index in range(3,n + 1):
            temp = pre_1 + pre_2
            pre_1 = pre_2
            pre_2 = temp

        return pre_2

if __name__ == '__main__':
    solution = Solution()
    print solution.climbStairs(4)