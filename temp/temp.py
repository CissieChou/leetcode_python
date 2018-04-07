# "%.2f" % 2.0

#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        length = int(sys.stdin.readline().strip())
        # 把每一行的数字分隔后转化成int列表
        road = sys.stdin.readline().strip()
        flags = [False] * (length + 2)
        result = 0
        for index, ch in enumerate(road):
            if flags[index] is False:
                if ch == ".":
                    if index == length - 3:
                        result += 1
                        break
                    else:
                        result += 1
                        flags[index+1] = True
                        flags[index+2] = True
        print(result)