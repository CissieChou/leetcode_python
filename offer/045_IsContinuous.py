# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) == 0:
            return False

        numbers = sorted(numbers)

        zero_count = 0
        for index, number in enumerate(numbers):
            if number == 0:
                zero_count += 1
            elif index > 0 and number == numbers[index-1]:
                return False

        other_numbers = numbers[zero_count:]

        min_number, max_number = other_numbers[0], other_numbers[-1]

        return max_number - min_number + 1 - len(other_numbers) - zero_count <= 0