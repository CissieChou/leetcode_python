class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        length = len(s)
        for index, ch in enumerate(s):
            ch_index = ord(ch) - 65 + 1
            result += ch_index * pow(26, length - index -1)

        return result

if __name__ == '__main__':
    print(pow(2,3))