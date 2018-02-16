from __future__ import print_function
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = [1]
        if n > 1:
            for i in range(n-1):
                temp = []
                count = 0
                cur_num = result[0]
                for index, num in enumerate(result):
                    if num == cur_num:
                        count += 1
                    else:
                        temp.append(count)
                        temp.append(cur_num)
                        cur_num = num
                        count = 1

                    if index == len(result) -1:
                        temp.append(count)
                        temp.append(num)
                result = temp

        result = [str(num) for num in result]
        return "".join(result)

if __name__ == '__main__':
    solution = Solution()
    print (solution.countAndSay(2))