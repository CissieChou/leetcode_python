class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version_list1 = [int(version) for version in version1.split(".")]
        version_list2 = [int(version) for version in version2.split(".")]

        if len(version_list1) < len(version_list2):
            version_list1 = version_list1 + [0]* (len(version_list2) - len(version_list1))
        else:
            version_list2 = version_list2 + [0]* (len(version_list1) - len(version_list2))

        index1 = 0
        index2 = 0
        for index in range(len(version_list1)):
            if version_list1[index] < version_list2[index]:
                return -1
            elif version_list1[index] > version_list2[index]:
                return 1

        return 0

if __name__ == '__main__':
    solution = Solution()
    version1 = "1.0"
    version2 = "01.1"
    print(solution.compareVersion(version1, version2))
