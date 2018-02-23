class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0

        final_result = ""

        a = list(a)
        b = list(b)

        while len(a) > 0 or len(b) > 0 or carry == 1:
            if len(a) > 0:
                single_a_num = int(a[-1])
                a.pop()
            else:
                single_a_num = 0

            if len(b) > 0:
                single_b_num = int(b[-1])
                b.pop()
            else:
                single_b_num = 0

            result = single_a_num + single_b_num + carry

            if result == 3:
                result = 1
                carry = 1
            elif result == 2:
                result = 0
                carry = 1
            else:
                carry = 0

            final_result += str(result)

        return final_result[::-1]



