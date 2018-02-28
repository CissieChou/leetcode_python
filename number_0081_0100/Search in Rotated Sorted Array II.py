class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = int(left + (right - left)/2)
            if nums[mid] == target:
                return True
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                right -= 1

        return nums[left] == target


if __name__ == '__main__':
    nums = [1,3,1,1,1]
    solution = Solution()
    print(solution.search(nums, 3))