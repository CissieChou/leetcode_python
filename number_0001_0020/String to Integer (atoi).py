from __future__ import print_function

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0

        INT_MAX = (1 << 31) - 1
        str = str.strip()
        positive = True

        if str[0] == "+":
            str = str[1:]
        elif str[0] == "-":
            str = str[1:]
            positive = False

        result = 0
        for ch in str:
            if ch.isdigit():
                ch_int = int(ch)
                result = result * 10 + ch_int
                if positive and result > INT_MAX:
                    result = INT_MAX
                    break
                elif not positive and result > INT_MAX + 1:
                    result = INT_MAX + 1
                    break
            else:
                break

        return result if positive else -result


if __name__ == '__main__':
    solution = Solution()

    string = " -1236788890676899"
    print(solution.myAtoi(string))