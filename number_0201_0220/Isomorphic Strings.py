class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dict = {}
        reverse_char_dict = {}
        if not len(s) == len(t):
            return False

        for index, ch in enumerate(s):
            if ch in char_dict:
                transfer_ch = char_dict[ch]
                if not transfer_ch == t[index]:
                    return False
            if t[index] in reverse_char_dict:
                raw_ch = reverse_char_dict[t[index]]
                if not raw_ch == ch:
                    return False
            else:
                reverse_char_dict[t[index]] = ch
                char_dict[ch] = t[index]

        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic("ab","aa"))

