from __future__ import print_function


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        ans = 0

        if len(height) == 0:
            return ans

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        while left < right:

            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1

        return ans

if __name__ == '__main__':
    solution = Solution()
    height = [2,0,2]
    print (solution.trap(height))
