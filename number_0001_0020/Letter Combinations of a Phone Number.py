from __future__ import print_function


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        digit_ch_list = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        final_results = []
        temp_result = []
        index = 0
        self.backtrack(digits, digit_ch_list, final_results, temp_result, index)

        return final_results

    def backtrack(self, digits, digit_ch_list, final_results, temp_result, index):
        if index == len(digits):
            final_results.append("".join(temp_result))
            return

        cur_ch_list = list(digit_ch_list[int(digits[index])])
        for cur_ch in cur_ch_list:
            temp_result.append(cur_ch)
            self.backtrack(digits, digit_ch_list,final_results,temp_result, index+1)
            temp_result.pop()


if __name__ == '__main__':
    solution = Solution()
    print (solution.letterCombinations("234"))