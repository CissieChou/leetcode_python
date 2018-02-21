class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = True

        if n < 0:
            flag = False
            n = abs(n)

        if n == 1:
            result = x
        elif n == 0:
            result = 1
        else:
            left_result = self.myPow(x, int(n / 2))
            if n % 2 == 0:
                result = left_result * left_result
            else:
                result = left_result * left_result * x

        if not flag:
            result = 1.0/result

        return result

if __name__ == '__main__':
    x = 2
    n = 2
    solution = Solution()
    print (solution.myPow(x, n))
