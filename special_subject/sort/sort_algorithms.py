# -*- coding:utf-8 -*-
import copy
import heapq

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
        self.doQuickSort2(A, 0, n - 1)
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

    def doQuickSort2(self, array, left, right):
        if left >= right:
            return
        j = self.partition(array, left, right)
        self.doQuickSort2(array, left, j - 1)
        self.doQuickSort2(array, j + 1, right)

    def partition(self, array, left, right):
        i = left + 1
        j = right

        num = array[left]
        while True:
            while i < right and array[i] <= num:
                i += 1
            while j > left and array[j] >= num:
                j -= 1
            if i >= j:
                break
            self.swap(array, i, j)

        self.swap(array, left, j)
        return j

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]

    def findKthLargest(self, array, k):
        k = len(array) - k
        left = 0
        right = len(array) - 1
        while left < right:
            j = self.partition(array, left, right)
            if j == k:
                break
            if j < k:
                left = j + 1
            else:
                right = j - 1
        return array[k]


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


class HeapSort():
    def heapSort(self, array):
        for index in range(len(array)/2 -1, -1, -1):
            self.adjust(array, index, len(array) -1)

        for end in range(len(array)-1, 0, -1):
            array[0], array[end] = array[end], array[0]
            self.adjust(array, 0, end - 1)

    def adjust(self, array, start, end):
        root = start

        child = root*2 + 1
        while child <= end:
            if child+1 <= end and array[child] < array[child+1]:
                child += 1

            if array[child] > array[root]:
                array[root], array[child] = array[child], array[root]
                root = child
            else:
                break

            child = root*2 + 1


class GetTopK():
    def getTopK(self, array, k):
        if len(array) <= k:
            return array

        topKHeap = copy.deepcopy(array[:k])
        for index in range(k/2 - 1, -1, -1):
            self.adjust(topKHeap, index, k - 1)

        for num in array[k:]:
            if num > topKHeap[0]:
                topKHeap[0] = num
            self.adjust(topKHeap, 0, k-1)

        return topKHeap

    def getKth(self, array, k):
        return self.getTopK(array, k)[0]

    def adjust(self, array, start, end):
        root = start

        child = root*2 + 1
        while child <= end:
            if child+1 <= end and array[child] > array[child+1]:
                child += 1

            if array[child] < array[root]:
                array[root], array[child] = array[child], array[root]
                root = child
            else:
                break

            child = root*2 + 1
    '''
    from leetcode
    '''
    # O(nlgn) time
    def findKthLargest1(self, nums, k):
        return sorted(nums, reverse=True)[k - 1]

    # O(nk) time, bubble sort idea, TLE
    def findKthLargest2(self, nums, k):
        for i in range(k):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    # exchange elements, time consuming
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums[len(nums) - k]

    # O(nk) time, selection sort idea
    def findKthLargest3(self, nums, k):
        for i in range(len(nums), len(nums) - k, -1):
            tmp = 0
            for j in range(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i - 1] = nums[i - 1], nums[tmp]
        return nums[len(nums) - k]

    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest4(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest5(self, nums, k):
        return heapq.nlargest(k, nums)[k - 1]


if __name__ == '__main__':
    mergeSort = MergeSort()
    case, length = [54,35,48,36,27,12,44,44,8,14,26,17,28],13
    # print (mergeSort.mergeSort(case, length))
    #
    # heapSort = HeapSort()
    # heapSort.heapSort(case)
    # print (case)

    getTopK = GetTopK()
    print (getTopK.getKth(case, 1))
    #
    quickSort = QuickSort()
    print (quickSort.findKthLargest(case, 2))
    quickSort.quickSort(case, len(case))
    print (case)
