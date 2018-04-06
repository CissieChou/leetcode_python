# -*- coding:utf-8 -*-
class Solution:
    result = 0
    temp = None
    def InversePairs(self, data):
        # write code here
        self.temp = [0] * len(data)
        self.mergesort(data, 0, len(data) - 1)
        self.result %= 1000000007
        return self.result

    def mergesort(self, data, left, right):

        if left >= right:
            return
        mid = left + (right - left)/2

        self.mergesort(data, left, mid)
        self.mergesort(data, mid+1, right)
        self.merge(data, left, mid, right)

    def merge(self, data, left, mid, right):
        first_pointer = left
        second_pointer = mid+1
        k = left
        while first_pointer <= mid and second_pointer <= right:
            if data[first_pointer] < data[second_pointer]:
                self.temp[k] = data[first_pointer]
                first_pointer += 1
            else:
                self.temp[k] = data[second_pointer]
                second_pointer += 1
                self.result += mid - first_pointer + 1
            k += 1

        self.result %= 1000000007
        while first_pointer <= mid:
            self.temp[k] = data[first_pointer]
            first_pointer += 1

        while second_pointer <= right:
            self.temp[k] = data[second_pointer]
            second_pointer += 1
            k += 1

        for index in range(left, right+1):
            data[index] = self.temp[index]
            k += 1

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,1,2]
    solution = Solution()
    print (solution.InversePairs(array))
