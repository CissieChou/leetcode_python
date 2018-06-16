class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seq_dict = set()
        result = set()
        for index in range(0, len(s) - 9):
            seq = s[index:index+10]
            if seq in seq_dict:
                result.add(seq)
            else:
                seq_dict.add(seq)
        return list(result)
