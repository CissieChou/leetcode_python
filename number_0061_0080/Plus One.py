class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0

        for index, num in enumerate(digits[::-1]):
            if index == 0:
                new_num = num + 1
            else:
                new_num = num + carry

            if new_num == 10:
                new_num = 0
                carry = 1
            else:
                carry = 0

            digits[len(digits) - index - 1] = new_num

            if carry == 0:
                break

        if carry == 1:
            digits.insert(0, 1)

        return digits