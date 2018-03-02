class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)

        if length == 0:
            return 0
        if length == 1:
            return triangle[0][0]

        dp = [1<<31]*len(triangle)
        dp[-1] = triangle[0][0]
        for row_index in range(1, len(triangle)):
            print(row_index, "--", dp)
            for col_index in range(row_index+1, 0, -1):
                if col_index == 1:
                    dp[-col_index] = dp[-col_index] + triangle[row_index][-col_index]
                else:
                    dp[-col_index] = min(dp[-col_index], dp[-col_index+1]) + triangle[row_index][-col_index]
                print(col_index, "||", dp)

        return min(dp)

if __name__ == '__main__':
    triangle = [[-1], [-2,-3]]
    solution = Solution()
    print(solution.minimumTotal(triangle))
