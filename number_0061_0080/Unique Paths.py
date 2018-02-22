class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        pre = [1] * m
        for i in range(1, n):
            temp = [0] * m

            for j in range(m):
                if j == 0:
                    temp[j] = pre[j]
                else:
                    temp[j] = temp[j - 1] + pre[j]

            pre = temp

        return pre[-1]