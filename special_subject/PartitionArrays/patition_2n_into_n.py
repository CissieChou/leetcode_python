#把一个2n的数组切分为两个n长度的数组，两个的和尽量接近
def patition_2n_into_n(nums):
    """
    令S(k, i)表示前k个元素中任意i个元素的和的集合。显然：
    注意公式中的数组序号是按照常规思路，从1开始的。
    S(k, 1) = {A[i] | 1<= i <= k}
    S(k, k) = {A[1]+A[2]+…+A[k]}
    S(k, i) = S(k-1, i) U {A[k] + x | x属于S(k-1, i-1) }
    :return:
    """
    total_sum = sum(nums)
    sub_sum = int(total_sum / 2)

    half_count = len(nums)/2
    flags = []
    for _ in range(len(nums) + 1):
        flags.append([False] * (sub_sum + 1))

    flags[0][0] = True

    for k, num in enumerate(nums):
        for i in range(k, 0, -1):
            if i > half_count:
                i = half_count
            for j in range(sub_sum):
                if j >= num and flags[i-1][j-num]:
                    flags[i][j] = True

    for j in range(sub_sum, -1, -1):
        if flags[half_count][j]:
            return total_sum - 2* j



# 是否能把一个数组切分为两个子集，两个的和相等
def patition_sum_into_sub(nums):
    total_sum = sum(nums)
    if total_sum & 1 == 1:
        return False

    sub_sum = int(total_sum / 2)
    dp = []
    for _ in range(len(nums) + 1):
        dp.append([False] * (sub_sum + 1))

    for i in range(len(nums) + 1):
        dp[i][0] = True

    for i, num in enumerate(nums, 1):
        for j in range(1, sub_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= num:
                dp[i][j] = (dp[i][j] or dp[i - 1][j - num])

    return dp[len(nums)][sub_sum]


#把一个数组切分为两个数组，其和尽量接近
def patition_sum_into_sub_sum(nums):

    total_sum = sum(nums)
    sub_sum = int(total_sum / 2)
    # dp[i][j]表示前i个数中和不超过j的最大sum
    dp = []
    for _ in range(len(nums) + 1):
        dp.append([0] * (sub_sum + 1))

    for i, num in enumerate(nums, 1):
        for j in range(1, sub_sum + 1):
            if j >= num:
                dp[i][j] = max(dp[i - 1][j], dp[i-1][j-num] + num)
            else:
                dp[i][j] = dp[i-1][j]

    return total_sum - 2 * dp[len(nums)][sub_sum]


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    print(patition_sum_into_sub_sum(nums))