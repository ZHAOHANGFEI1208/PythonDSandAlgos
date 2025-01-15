## 算法思路
# 搜索   暴力全排列搜索所有字符串的顺序，比较大小，得出最终答案。
# 贪心   321 和 32 相比 32321》32132

## 代码实现
# 自定义比较函数
# 字典序
# 排序
# 反转


from functools import cmp_to_key

# 自定义比较函数
def compare(x, y):
    # 比较 x + y 和 y + x 的大小，决定 x 和 y 的排序
    if x + y > y + x:
        return -1  # x 应该排在 y 前面
    elif x + y < y + x:
        return 1   # y 应该排在 x 前面
    else:
        return 0   # x 和 y 相等

# 输入处理
n = int(input())  # 读取整数个数
list1 = input().split()  # 读取整数列表

# 排序
list1.sort(key=cmp_to_key(compare))

# 输出结果
print("".join(list1))

## 部分得分
# num = int(input())
# list1 = input().split()

# list1.sort()
# list1.reverse()
# if len(list1) == 1 and list[0] == 0:
#     print(0)
# else:
#     print("".join(map(str,list1)))