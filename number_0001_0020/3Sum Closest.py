from __future__ import print_function

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        min_diffecence = 1 << 31 - 1
        result = 0
        nums_len = len(nums)

        for index in range(nums_len-2):
            left = index + 1
            right = nums_len - 1

            while left < right:

                cur_sum = nums[index] + nums[left] + nums[right]
                difference = cur_sum - target
                cur_difference = abs(difference)

                if cur_difference < min_diffecence:
                    result = cur_sum
                    min_diffecence = cur_difference

                if difference == 0:
                    break
                elif difference < 0:
                    left += 1
                else:
                    right -= 1

        return result

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,0]
    print (solution.threeSumClosest(nums,-100))