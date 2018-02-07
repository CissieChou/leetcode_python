class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1

        for index in range(len(haystack) - len(needle) + 1):
            if haystack[index:index + len(needle)] == needle:
                return index

        return -1

    def strStr_KMP(self, t, p):
        pnext, i, j = self.gen_pnext(p), 0, 0
        n, m = len(t), len(p)
        while j < n and i < m:
            if i == -1 or t[j] == p[i]:
                j, i = j + 1, i + 1
            else:
                i = pnext[i]
        if i == m:
            return j - i
        return -1


    def gen_pnext(self, p):
        i, k, m = 0, -1, len(p)
        pnext = [-1] * m
        while i < m - 1:
            if k == -1 or p[i] == p[k]:
                i, k = i + 1, k + 1
                if p[i] == p[k]:
                    pnext[i] = pnext[k]
                else:
                    pnext[i] = k
            else:
                k = pnext[k]
        return pnext