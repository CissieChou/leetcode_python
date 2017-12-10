class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch_index_map = {}
        left_max_index = 0
        right_max_index = 0
        left_index = 0
        result = 0
        for index, ch in enumerate(s):
            if ch in ch_index_map:
                left_index = max(ch_index_map[ch] + 1, left_index)
            if index - left_index > right_max_index - left_max_index:
                left_max_index = left_index
                right_max_index = index
                result = right_max_index - left_max_index + 1
            ch_index_map[ch] = index

        return result



if __name__ == '__main__':
    solution = Solution()
    s = "pwwkew"
    print solution.lengthOfLongestSubstring(s)