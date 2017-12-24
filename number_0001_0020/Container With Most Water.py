from __future__ import print_function


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        left_index = 0
        right_index = len(height) - 1
        max_area = 0
        while left_index < right_index:
            cur_area = (right_index - left_index) * min(height[right_index], height[left_index])
            if cur_area > max_area:
                max_area = cur_area

            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1

        return max_area


if __name__ == '__main__':
    solution = Solution()
    height = [1, 1]
    print (solution.maxArea(height))