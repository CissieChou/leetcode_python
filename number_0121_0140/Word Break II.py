class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        wordDictSet = set()
        for word in wordDict:
            wordDictSet.add(word)

        memory_dict = {}
        return self.backTrack(s, wordDictSet, 0, memory_dict)

    def backTrack(self, s, wordDict, start, memory_dict):
        if s[start:] in memory_dict:
            return memory_dict[s[start:]]

        results = []
        if start == len(s):
            results.append("")
            return results

        for index in range(start, len(s)):
            if s[start:index+1] in wordDict:
                pre_results = self.backTrack(s, wordDict, index+1, memory_dict)
                for pre_result in pre_results:
                    cur_str = s[start:index+1] + (" " + pre_result if len(pre_result) > 0 else "")
                    results.append(cur_str)

        memory_dict[s[start:]] = results
        return results
