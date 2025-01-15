# 题意是有一个数等于其它两个数之和
# 你求的是两个数的和等于第三个数
# 例如 3 + 4 = 7，2 + 5 = 7 按照题意应该只计算7一个数，但是在代码里7被计算了两次答案，要对答案去重

"""
num = int(input())
list1 = list(map(int, input().split(" ")))
howmuch:int = 0
for index in range(num):
    for index2 in range(index+1,num):
        if (list1[index] + list1[index2]) in list1:
            howmuch += 1
print(howmuch)
"""

num = int(input())
list1 = list(map(int, input().split(" ")))
set1 = set(list1)
set2 = set()
count = 0
for index in range(num):
    for index2 in range(index+1,num):
        set2.add(list1[index] + list1[index2])
for number in list1:
    if number in set2:
        count += 1
print(count)