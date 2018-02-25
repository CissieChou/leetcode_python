class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return

        left = 0
        right = len(nums) - 1

        index = 0
        while index <= right:
            while nums[index] == 2 and index < right:
                temp = nums[index]
                nums[index] = nums[right]
                nums[right] = temp
                right -= 1
            while nums[index] == 0 and index > left:
                temp = nums[index]
                nums[index] = nums[left]
                nums[left] = temp
                left += 1
            index += 1

if __name__ == '__main__':
    nums = [2,0]
    solution = Solution()
    solution.sortColors(nums)
    print(nums)