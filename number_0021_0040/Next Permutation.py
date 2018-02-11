from __future__ import print_function
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return

        i = -1
        for index in list(range(1, len(nums)))[::-1]:
            if nums[index] > nums[index-1]:
                i = index-1
                break

        if i >= 0:
            j = -1
            for index in list(range(i+1, len(nums))):
                if nums[index] > nums[i]:
                    j = index
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        nums[i+1:] = reversed(nums[i+1:])


if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,2]
    for i in range(2):
        solution.nextPermutation(nums)
        print (nums)

