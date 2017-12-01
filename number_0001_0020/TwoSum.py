from __future__ import print_function
from __future__ import absolute_import
from structure import ListNode


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dif_index_dict = {}
        for index, num in enumerate(nums):
            if num in dif_index_dict:
                return [dif_index_dict[num], index]
            else:
                dif_index_dict[target-num] = index


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print (solution.twoSum(nums=nums,target=target))