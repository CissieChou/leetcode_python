class Solution(object):
    '''
    A = [2,3,1,1,4], return true.
    A = [3,2,1,0,4], return false.
    '''
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True

        max_index = 0
        for index, num in enumerate(nums[:-1]):
            if index > max_index:
                return False

            if index + num >= len(nums) - 1:
                return True

            max_index = max(index + num, max_index)

        return max_index >= len(nums) - 1

if __name__ == '__main__':
    nums = [3,2,1,0,4]
    solution = Solution()

    print (solution.canJump(nums))