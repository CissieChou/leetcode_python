from __future__ import print_function

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x%10 == 0 and not x == 0):
            return False

        left = x
        right = 0

        while left > right:
            right = right * 10 + left % 10
            left /= 10

        if left == right or right/10 == left:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    x = 2058338502
    print (solution.isPalindrome(x))