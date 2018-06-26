class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k
        left = 0
        right = len(nums) - 1
        while left < right:
            j = self.partition(nums, left, right)

            if j == k:
                break
            elif j > k:
                right = j - 1
            else:
                left = j + 1

        return nums[k]


    def partition(self, nums, left, right):
        judge_num = nums[left]
        i = left + 1
        j = right

        while True:
            while i < right and nums[i] <= judge_num:
                i += 1
            while j > left and nums[j] >= judge_num:
                j -= 1
            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[j] = nums[j], nums[left]
        return j

if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,1,5,6,4]
    print(solution.findKthLargest(nums, 2))
