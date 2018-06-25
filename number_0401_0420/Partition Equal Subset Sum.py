class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # dp[i][j] means pre i nums can sum j

        total_sum = sum(nums)
        if total_sum & 1 == 1:
            return False

        sub_sum = int(total_sum / 2)
        dp = []
        for _ in range(len(nums) + 1):
            dp.append([False] * (sub_sum + 1))

        for i in range(len(nums)+1):
            dp[i][0] = True

        for i, num in enumerate(nums, 1):
            for j in range(1, sub_sum + 1):
                dp[i][j] = dp[i-1][j]
                if j >= num:
                    dp[i][j] = (dp[i][j] or dp[i-1][j-num])

        return dp[len(nums)][sub_sum]

if __name__ == '__main__':
    nums = [1,2,5]
    solution = Solution()
    print(solution.canPartition(nums))