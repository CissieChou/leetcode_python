class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        result = 1 << 32
        cur_sum = 0
        left = 0
        for index, num in enumerate(nums):
            cur_sum += num
            while cur_sum >= s:
                result = min(result, index - left + 1)
                cur_sum -= nums[left]
                left += 1

        if result == 1 << 32:
            return 0
        else:
            return result

if __name__ == '__main__':
    s = 4
    nums = [3,5]