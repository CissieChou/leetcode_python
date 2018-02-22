class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        pre = [0] * len(grid[0])

        for i in range(len(grid)):
            temp = [0] * len(grid[0])
            for j in range(len(grid[0])):

                if j == 0:
                    temp[j] = pre[j] + grid[i][j]
                elif i == 0:
                    temp[j] = temp[j-1] + grid[i][j]
                else:
                    temp[j] = min(pre[j], temp[j-1]) + grid[i][j]

            pre = temp

        return pre[-1]