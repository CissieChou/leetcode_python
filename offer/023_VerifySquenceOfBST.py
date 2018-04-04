# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        left_tree_end = -1

        for index, num in enumerate(sequence):
            if num < root and sequence[index+1] >= root:
                left_tree_end = index
                break

        for index in range(left_tree_end + 1):
            if sequence[index] > root:
                return False

        for index in range(left_tree_end+1, len(sequence) - 1):
            if sequence[index] <= root:
                return False

        left_flag = True
        right_flag = True
        if len(sequence[:left_tree_end+1]) > 0:
            left_flag = self.VerifySquenceOfBST(sequence[:left_tree_end+1])
        if len(sequence[left_tree_end+1:-1]) > 0:
            right_flag = self.VerifySquenceOfBST(sequence[left_tree_end+1:-1])

        return left_flag and right_flag


if __name__ == '__main__':
    sequence = [4,6,7,5]
    solution = Solution()
    print(solution.VerifySquenceOfBST(sequence))