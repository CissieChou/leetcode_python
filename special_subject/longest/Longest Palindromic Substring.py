class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""

        left = 0
        right = 0
        length_max = 0
        for index in range(len(s)):
            length_odd = self.getPalindromicLength(s, index, index)
            length_even = self.getPalindromicLength(s, index, index+1)
            length_max_temp = max(length_odd, length_even)
            if length_max_temp > length_max:
                left = int(index - (length_max_temp - 1) / 2)
                right = int(index + length_max_temp / 2)

        return s[left:right+1]

    def getPalindromicLength(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1
