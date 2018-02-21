class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result_dict = {}

        for single_str in strs:
            ch_list = list(single_str)
            ch_list.sort()
            sorted_str = "".join(ch_list)
            if sorted_str not in result_dict:
                result_dict[sorted_str] = []
            result_dict[sorted_str].append(single_str)

        return list(result_dict.values())