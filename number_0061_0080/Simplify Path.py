class Solution(object):
    '''
    path = "/home/", => "/home"
    path = "/a/./b/../../c/", => "/c"
    '''
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.strip("/")
        path_list = path.split("/")

        result = []
        for single_item in path_list:
            if single_item == "..":
                if len(result) > 0:
                    result.pop()
            elif (not single_item == ".") and (len(single_item) > 0):
                result.append(single_item)

        return "/" + "/".join(result)

if __name__ == '__main__':
    solution = Solution()
    print solution.simplifyPath("/a/./b/../../c/")
