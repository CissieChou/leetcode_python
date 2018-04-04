# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []

        results = []
        flags = [False] * len(ss)
        ss = sorted(ss)
        self.backTrack(ss, results, flags, [])
        return results

    def backTrack(self, ss, results, flags, single_result):
        if len(single_result) == len(ss):
            results.append("".join(single_result))
            return

        for index in range(len(ss)):
            if index > 0 and ss[index] == ss[index-1] and flags[index-1] == False:
                continue
            if flags[index] == True:
                continue
            flags[index] = True
            self.backTrack(ss, results, flags, single_result + [ss[index]])
            flags[index] = False


if __name__ == '__main__':
    ss = "a"
    solution = Solution()
    print(solution.Permutation(ss))