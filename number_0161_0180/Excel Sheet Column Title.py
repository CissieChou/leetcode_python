class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        base_num = 65
        result = ""
        while n > 0:
            n -= 1
            xremainder = n % 26
            quotient = n//26
            n = quotient

            result = chr(int(xremainder + base_num)) + result

        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToTitle(701))
