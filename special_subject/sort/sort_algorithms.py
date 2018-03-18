# -*- coding:utf-8 -*-

class BubbleSort:
    def bubbleSort(self, A, n):
        # write code here
        for i in range(n-1):
            for j in range(n - i -1):
                if A[j] > A[j+1]:
                    temp = A[j+1]
                    A[j+1] = A[j]
                    A[j] = temp
        return A

# -*- coding:utf-8 -*-

class SelectionSort:
    def selectionSort(self, A, n):
        # write code here
        for i in range(n):
            max_index = 0
            max_num = A[0]
            for j in range(1, n - i):
                if A[j] > max_num:
                    max_num = A[j]
                    max_index = j

            A[max_index] = A[n-i-1]
            A[n-i-1] = max_num

        return A

# -*- coding:utf-8 -*-

class InsertionSort:
    def insertionSort(self, A, n):
        # write code here
        for i in range(1,n):
            cur = A[i]
            j = i - 1
            while cur < A[j] and j >= 0:

                A[j+1] = A[j]
                j -= 1

            A[j+1] = cur

        return A

# -*- coding:utf-8 -*-

class ShellSort:
    def shellSort(self, A, n):
        # write code here
        dk = n/2
        while dk >= 1:
            for i in range(dk, n):
                cur = A[i]
                j = i - dk
                while cur < A[j] and j >= 0:
                    A[j+dk] = A[j]
                    j -= dk

                A[j+dk] = cur

            dk /= 2

        return A

# -*- coding:utf-8 -*-

class QuickSort:
    def quickSort(self, A, n):
        # write code here
        self.doQuickSort(A, 0, n - 1)
        return A

    def doQuickSort(self, A, left,right):
        if right <= left:
            return

        judge_num = A[left]
        left_point = left
        for i in range(left + 1, right + 1):
            if judge_num > A[i]:
                left_point += 1
                temp = A[left_point]
                A[left_point] = A[i]
                A[i] = temp

        A[left] = A[left_point]
        A[left_point] = judge_num
        self.doQuickSort(A, left, left_point - 1)
        self.doQuickSort(A, left_point + 1, right)

# -*- coding:utf-8 -*-

class MergeSort:
    def mergeSort(self, A, n):
        # write code here
        self.mergeSortFun(A, 0, n-1)
        return A

    def mergeSortFun(self, A, left, right):
        mid = left + (right - left)/2
        if left < right:
            self.mergeSortFun(A, left, mid)
            self.mergeSortFun(A, mid + 1, right)
            self.mergeSortFun2(A, left, mid, right)

    def mergeSortFun2(self, A, left, mid, right):
        temp = []
        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if A[i] < A[j]:
                temp.append(A[i])
                i += 1
            else:
                temp.append(A[j])
                j += 1

        while i <= mid:
            temp.append(A[i])
            i += 1

        while j <= right:
            temp.append(A[j])
            j += 1
        for index, num in enumerate(temp, left):
            A[index] = num

if __name__ == '__main__':
    mergeSort = MergeSort()
    case, length = [54,35,48,36,27,12,44,44,8,14,26,17,28],13
    print mergeSort.mergeSort(case, length)
