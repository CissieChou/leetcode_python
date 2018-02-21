from __future__ import print_function

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        results = [0] * (len(num1) + len(num2))

        for i, num1_single in enumerate(reversed(num1)):
            for j, num2_single in enumerate(reversed(num2)):
                temp_result = int(num1_single) * int(num2_single)
                results[i + j] += temp_result

                results[i + j + 1] += results[i + j] / 10
                results[i + j] = results[i + j] % 10

        if len(results) >= 1:
            result = "".join([str(num) for num in results])
            result = result[0] + result[1:].rstrip("0")

        return result[::-1]

if __name__ == '__main__':
    solution = Solution()
    print (solution.multiply("123","7809"))
    print (123*7809)