class Solution(object):
    # this algorithm will fail in python
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        bit_length = 64
        common_count = 3

        for i in range(bit_length):
            sum = 0
            for num in nums:
                if ((num >> i) & 1) == 1:
                    sum += 1
                    sum %= common_count
            res |= (sum << i)
        return res


if __name__ == '__main__':
    nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
    solution = Solution()
    print solution.singleNumber(nums)