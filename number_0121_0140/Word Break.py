class Solution(object):
    result = False
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """


        wordDictSet = set()
        for item in wordDict:
            wordDictSet.add(item)
        flags = [False] * len(s)

        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] in wordDictSet and (j == 0 or flags[j-1]):
                    flags[i] = True

        return flags[len(s)-1]


if __name__ == '__main__':
    solution = Solution()

    s = "leetcode"
    wordDict = ["leet", "code"]
    solution.wordBreak(s, wordDict)