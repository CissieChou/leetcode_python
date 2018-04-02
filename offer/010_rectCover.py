# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return number
        pre = 1
        tail = 2

        for _ in range(3,number+1):
            temp = pre + tail
            pre = tail
            tail = temp

        return tail

if __name__ == '__main__':
    solution = Solution()
    print(solution.rectCover(3))