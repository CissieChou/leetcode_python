from __future__ import print_function


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int_32_max = (1 << 31) - 1

        signal = (x >= 0)
        final_sum = 0
        for index, num in enumerate(str(abs(x))[::-1]):
            final_sum = final_sum * 10 + int(num)
            if final_sum > int_32_max:
                return 0

        return final_sum if signal else -final_sum


if __name__ == '__main__':
    solution = Solution()
    x = -123
    print(solution.reverse(x))
    print((1 << 31) - 1)
