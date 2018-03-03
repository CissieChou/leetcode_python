class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result = 0
        nums = []
        for ch in tokens:
            if ch not in ["+","-","*","/"]:
                nums.append(int(ch))
            else:
                pre_1_num = nums.pop()
                pre_2_num = nums.pop()
                if ch == "+":
                    nums.append(pre_1_num + pre_2_num)
                elif ch == "-":
                    nums.append(pre_2_num - pre_1_num)
                elif ch == "*":
                    nums.append(pre_1_num * pre_2_num)
                else:
                    nums.append(int(pre_2_num / pre_1_num))
            print nums

        return nums.pop()

if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    solution = Solution()
    print solution.evalRPN(tokens)
    print -6/132