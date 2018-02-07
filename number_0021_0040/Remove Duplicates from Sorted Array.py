from __future__ import print_function
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        left = 0
        for right, num in enumerate(nums):
            if num == nums[left]:
                continue
            else:
                left += 1
                nums[left] = num

        print (nums)
        return left + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([1,1,2,2,3,4,4,4,5]))