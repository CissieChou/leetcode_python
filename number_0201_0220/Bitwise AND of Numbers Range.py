class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0

        count = 1

        while not m == n:
            m >>= 1
            n >>= 1
            count <<= 1

        return n * count
