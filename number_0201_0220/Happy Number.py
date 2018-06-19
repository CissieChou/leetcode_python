class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = set()
        while not n == 1:
            num_str = str(n)
            result = 0
            for single_num in num_str:
                num = int(single_num)
                result += pow(num, 2)
            if result in temp:
                return False
            else:
                temp.add(result)

            n = result

        return True
