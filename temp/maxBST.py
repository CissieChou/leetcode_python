# coding=utf-8
import sys
if __name__ == "__main__":
    [n, m] = [int(x) for x in sys.stdin.readline().strip().split()]
    data_list = []
    for i in range(n):
        data_list.append([int(x) for x in sys.stdin.readline().strip().split()])
    value_list = [[i, int(x)] for i, x in enumerate(sys.stdin.readline().strip().split())]
    value_dict = {}
    data_list.sort(key=lambda x : (x[1], x[0]), reverse=True)
    value_list.sort(key = lambda x : x[1], reverse=True)
    i = 0; j = 0
    while i < n and j < m:
        if value_list[j][1] >= data_list[i][0]:
            if value_list[j][0] not in value_dict:
                value_dict[value_list[j][0]] = data_list[i][1]
            elif value_dict[value_list[j][0]] < data_list[i][1]:
                value_dict[value_list[j][0]] = data_list[i][1]
            j += 1
        else: i += 1
    for i in range(m):
        print(value_dict[i])