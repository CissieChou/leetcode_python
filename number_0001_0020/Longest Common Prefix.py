from __future__ import print_function


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort(key=lambda single_str:len(single_str),reverse=True)

        longest_prefix = strs[0]

        for index, single_str in enumerate(strs[1:]):
            while not single_str.startswith(longest_prefix):
                longest_prefix = longest_prefix[:len(longest_prefix) - 1]

        return longest_prefix


if __name__ == '__main__':
    solution = Solution()
    strs = ["acbd","ac","acd"]
    print(solution.longestCommonPrefix(strs))