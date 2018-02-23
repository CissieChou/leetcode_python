class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(matrix)
        if len(matrix) > 0 and len(matrix[0]) == 0:
            return False

        while left < right:
            mid = left + (right - left) /2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.binarySearch(matrix[mid], target)
            elif target < matrix[mid][0]:
                right = mid
            else:
                left = mid + 1

        return False

    def binarySearch(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left)/2
            if nums[mid] == target:
                 return True
            elif nums[mid] < target:
                 left = mid + 1
            else:
                 right = mid

        return False


if __name__ == '__main__':
    matrix = [[1], [3], [5]]
    solution = Solution()
    print (solution.searchMatrix(matrix, 5))

