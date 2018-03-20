class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        self.backTrack(s, results, [], 0)
        return results

    def backTrack(self, s, results, single_result, start):
        if len(single_result) > 4:
            return
        if len(single_result) == 4 and start == len(s):
            results.append(".".join(single_result))

        for index in range(3):
            if index + start >= len(s):
                continue

            cur_str = s[start:start+index+1]
            if int(cur_str) > 255 or (index > 0 and cur_str[0] == "0"):
                continue
            self.backTrack(s, results, single_result + [cur_str], start + index + 1)


if __name__ == '__main__':
    s = "010010"
    solution = Solution()
    print(solution.restoreIpAddresses(s))
