class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        results = []
        self.backTrack(s, 0, [], results)
        return results


    def backTrack(self, s, start, single_result, results):
        if start == len(s):
            if len(single_result) > 0:
                results.append(single_result)
            return

        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                self.backTrack(s, i + 1, single_result + [s[start:i+1]], results)


    def isPalindrome(self, s, left, right):
        while left < right:
            if not s[left] == s[right]:
                return False
            left += 1
            right -= 1

        return True