# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    ch_dict = {}
    s = ""
    def FirstAppearingOnce(self):
        # write code here
        for ch in self.s:
            if self.ch_dict[ch] == 1:
                return ch

        return "#"

    def Insert(self, char):
        # write code here
        self.s += char
        if char not in self.ch_dict:
            self.ch_dict[char] = 1
        else:
            self.ch_dict[char] = -1

if __name__ == '__main__':
    solution = Solution()
    s = "BabyBaby"
    for m in s:
        solution.Insert(m)
        print (solution.FirstAppearingOnce())