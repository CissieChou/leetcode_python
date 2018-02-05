class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not len(s) % 2 == 0:
            return False
        flag = True
        ch_list = list(s)
        stack = []

        ope_dict = {")":"(","}":"{","]":"["}
        for ch in ch_list:
            if ch not in ope_dict:
                stack.append(ch)
            elif not (len(stack) > 0 and stack.pop() == ope_dict[ch]):
                    flag = False
                    break

        if len(stack) > 0:
            flag = False
        return flag