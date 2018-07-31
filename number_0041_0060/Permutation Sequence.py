class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = [1] * (n + 1)
        for index, num in enumerate(range(1, n + 1), 1):
            factorial[index] = factorial[index - 1] * num

        result = ""

        k -= 1
        numbers = list(range(1, n + 1))
        for index in range(n):
            number = int(k/factorial[n - index - 1])
            result += str(numbers[number])
            numbers.remove(numbers[number])
            k -= number * factorial[n - index - 1]

        return result

if __name__ == '__main__':
    solution = Solution()
    print (solution.getPermutation(3,3))