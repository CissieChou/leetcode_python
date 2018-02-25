class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        result_index = m + n - 1

        index_1 = m - 1
        index_2 = n - 1
        while index_1 >= 0 or index_2 >= 0:
            if index_1 < 0:
                nums1[result_index] = nums2[index_2]
                result_index -= 1
                index_2 -= 1
            elif index_2 < 0:
                break
            else:
                if nums1[index_1] > nums2[index_2]:
                    nums1[result_index] = nums1[index_1]
                    index_1 -= 1
                else:
                    nums1[result_index] = nums2[index_2]
                    index_2 -= 1
                result_index -= 1

