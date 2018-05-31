class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if len(grid) == 0:
            return 0
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.walk(grid, i, j)
                    result += 1

        return result

    def walk(self, grid, row,col):

        if row < 0 or row > len(grid) - 1:
            return
        if col < 0 or col > len(grid[0]) - 1:
            return
        if grid[row][col] in ['0','2']:
            return
        else:
            grid[row][col] = '2'
            self.walk(grid, row-1, col)
            self.walk(grid, row+1, col)
            self.walk(grid, row, col -1)
            self.walk(grid, row, col +1)


if __name__ == '__main__':
    x = [
        [1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,1,0,1]
    ]

    solution = Solution()
    print(solution.numIslands(x))
