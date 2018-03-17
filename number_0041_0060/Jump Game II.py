class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        index = 0
        cur_distance = nums[0]
        count = 1

        while index + cur_distance < len(nums) - 1:
            next_index = index + 1
            for temp_index in range(index + 2, index + cur_distance + 1):
                if temp_index + nums[temp_index] > next_index + nums[next_index]:
                    next_index = temp_index

            index = next_index
            cur_distance = nums[next_index]
            count += 1

        return count

if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,0,1,4]
    print(solution.jump(nums))