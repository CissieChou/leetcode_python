from __future__ import print_function
import copy

class Solution:
    def nSum(self,nums,target,single_result,total_results, n):
        if len(nums) < n or nums[-1] * n < target or nums[0] * n > target or n < 2:
            return

        if n == 2:
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:

                    total_results.append(single_result + [nums[left],nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        else:
            for index in range(len(nums) - n + 1):
                if index > 0 and nums[index] == nums[index -1]:
                    continue
                self.nSum(nums[index+1:],target-nums[index],single_result + [nums[index]],total_results,n-1)

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        total_results = []
        single_result = []
        self.nSum(nums,target,single_result,total_results,4)
        return total_results


if __name__ == '__main__':
    solution = Solution()
    print (solution.fourSum([1, 0, -1, 0, -2, 2],0))