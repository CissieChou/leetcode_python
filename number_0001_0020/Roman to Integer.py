from __future__ import print_function


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        ch_num_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 100,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        sum_result = 0
        for index, ch in enumerate(s):
            if index < len(s) - 1:
                if ch_num_dict[ch] < ch_num_dict[s[index +1]]:
                    sum_result -= ch_num_dict[ch]
                else:
                    sum_result += ch_num_dict[ch]
            else:
                sum_result += ch_num_dict[ch]

        return sum_result


if __name__ == '__main__':
    solution = Solution()
    s = "M"
    print (solution.romanToInt(s))
