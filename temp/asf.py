def func(d_list, p_list, m):
    if m > 10000000:
        print(p_list[-1])
    else:
        dp = [0] * (m + 1)
        # 大数不好处理

        for i, d in enumerate(d_list):
            for j in range(m,d-1,-1):
                dp[j] = max(dp[j],dp[j-d_list[i]]+p_list[i])
        print(dp[-1])

# coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n_m = sys.stdin.readline().strip()
    n = int(n_m.split()[0])
    m = int(n_m.split()[1])

    d_list = [0] * n
    p_list = [0] * m

    for i in range(n):
        d, p = sys.stdin.readline().strip().split()
        d = int(d)
        p = int(p)
        d_list[i] = d
        p_list[i] = p

    m_list = list(map(int, sys.stdin.readline().strip().split()))
    for m in m_list:
        func(d_list, p_list, m)
