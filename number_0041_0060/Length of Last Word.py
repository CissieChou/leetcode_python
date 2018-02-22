class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()

        if len(s) == 0:
            return 0
        result = 0
        for index in range(len(s) - 1, - 1, -1):
            if s[index] == " ":
                break
            result += 1

        return result