class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        pre = [0] * len(obstacleGrid[0])

        for i in range(0, len(obstacleGrid)):
            temp = [0] * len(obstacleGrid[0])
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    temp[j] = 0
                    continue

                if i == 0 and j == 0:
                    temp[j] = 1
                elif j == 0:
                    temp[j] = pre[j]
                else:
                    temp[j] = temp[j - 1] + pre[j]

            pre = temp

        return pre[-1]
