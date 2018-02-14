from __future__ import print_function


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_index = self.bisearch(nums, target, True)
        right_index = self.bisearch(nums, target, False)

        if left_index > len(nums) - 1 or not nums[left_index] == target:
            return [-1, -1]

        return [left_index, right_index - 1]

    def bisearch(self, nums, target, is_left):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) / 2

            if nums[mid] > target or (is_left and nums[mid] == target):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    solution = Solution()
    print (solution.searchRange([1, 3, 3], 3))
