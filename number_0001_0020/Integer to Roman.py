from __future__ import print_function


# remain to be understood
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10]

    def intToRoman2(self, num):
        """

        :param num:
        :return:
        """
        if num < 0 or num > 3999:
            return ""

        result = ""
        roman_value_tuples = [("M",1000),("CM",900),("D",500),("CD",400),
                           ("C",100),("XC",90),("L",50),("XL",40),
                           ("X",10),("IX",9),("V",5),("IV",4),("I",1)]
        index = 0
        while num > 0:
            while num >= roman_value_tuples[index][1]:
                num -= roman_value_tuples[index][1]
                result += roman_value_tuples[index][0]
            index +=1

        return result


if __name__ == '__main__':
    solution = Solution()
    num = 10
    print (solution.intToRoman(num))