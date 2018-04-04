# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return

        for i in range(len(array)):
            if not self.is_even(array[i]):
                temp = array[i]
                j = i - 1
                while j >= 0 and self.is_even(array[j]):
                    array[j+1] = array[j]
                    j -= 1
                array[j+1] = temp

    def is_even(self, num):
        return num & 1 == 0

if __name__ == '__main__':
    solution = Solution()
    array = [1,2,3,4,5,6,7]
    solution.reOrderArray(array)
    print(array)