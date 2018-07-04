class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s) == len(t):
            return False

        s_dict = {}
        for ch in s:
            if ch not in s_dict:
                s_dict[ch] = 0
            s_dict[ch] = s_dict[ch] + 1

        t_dict = {}
        for ch in t:
            if ch not in t_dict:
                t_dict[ch] = 0
            t_dict[ch] = t_dict[ch] + 1

        for ch, count in s_dict.items():
            if ch not in t_dict or not t_dict[ch] == count:
                return False

        return True


