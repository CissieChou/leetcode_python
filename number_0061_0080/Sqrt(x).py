class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        left = 1
        right = x

        while True:
            mid = left + (right - left) / 2
            cur_product = mid * mid

            next_product = (mid + 1) * (mid +1)

            if cur_product == x or (cur_product < x < next_product):
                return mid
            elif cur_product < x:
                left = mid + 1
            else:
                right = mid
        '''
        # r = x
        # while r * r > x:
        #     r = (r + x / r) / 2
        # return r

        r = x
        while r * r > x:
            r = (r + x / r) / 2

        return r

if __name__ == '__main__':
    solution = Solution()
    print (solution.mySqrt(26))
