from __future__ import print_function

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg_flag = not ((dividend < 0) == (divisor < 0))

        dividend, divisor = abs(dividend), abs(divisor)

        raw_divisor = divisor

        result = 0
        left = 0

        while dividend >= divisor:
            dividend = dividend - divisor
            result += (1 << left)
            left += 1
            divisor = divisor << 1

        right = left
        while dividend > 0:
            if divisor < raw_divisor:
                break
            elif dividend >= divisor:
                dividend = dividend - divisor
                result += (1 << right)
            else:
                right -= 1
                divisor = divisor >> 1

        if neg_flag:
            result = -result

        return result

    def divide2(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

if __name__ == '__main__':
    solution = Solution()
    print(solution.divide(10, 1))