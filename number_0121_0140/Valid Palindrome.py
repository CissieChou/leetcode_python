class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        right = len(s) - 1
        left = 0

        while left < right:
            while not s[left].isalnum() and left < len(s) - 1:
                left += 1

            while not s[right].isalnum() and right > 0:
                right -= 1

            if left == right:
                break

            if not s[left] == s[right]:
                return False
            else:
                left += 1
                right -= 1

        return True

if __name__ == '__main__':
    s = "......a....."
    solution = Solution()
    print solution.isPalindrome(s)