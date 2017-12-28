from __future__ import print_function


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_value_tuples = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
                              ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
                              ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]

        length = len(s)

        result = 0
        index = 0

if __name__ == '__main__':
    solution = Solution()
    s = "M"
    print (solution.romanToInt(s))
