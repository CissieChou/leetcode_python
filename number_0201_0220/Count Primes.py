class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        flags = [False] * (n)
        count = 0
        for i in range(2, n):
            if not flags[i]:
                j = 2
                while i*j < n:
                    flags[i*j] = True
                    j += 1
                count += 1

        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(10))

