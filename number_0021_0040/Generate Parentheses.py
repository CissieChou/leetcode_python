class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        self.backtrack(result, "", 0, 0, n)
        return result

    def backtrack(self, result, single_str, left, right, n):
        if left + right == n*2:
            result.append(single_str)
            return

        if left < n:
            self.backtrack(result, single_str + "(", left + 1, right, n)

        if right < left:
            self.backtrack(result, single_str + ")", left, right+1, n)
