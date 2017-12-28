from __future__ import print_function


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        left_index = right_index = 0
        for index, ch in enumerate(s):
            length1 = self.get_palindrome(s, index, index)
            length2 = self.get_palindrome(s, index, index+1)
            length = max(length1, length2)
            print(length, ch)
            if length > max_length:
                max_length = length
                left_index = int(index - (length - 1)/2)
                right_index = int(index + length/2)

        return s[left_index:right_index+1]

    def get_palindrome(self, s, left, right):
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1


if __name__ == '__main__':
    s = "babad"
    solution = Solution()
    print(solution.longestPalindrome(s))