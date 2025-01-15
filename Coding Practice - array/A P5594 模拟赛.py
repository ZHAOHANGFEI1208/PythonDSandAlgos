# 算法思路
# -----------------------------------------------------------------------------
# 发现规律 2.1 5.2 7.3 
# 借助集合特性，遍历每一个人：A第二天做第一套，则在第二天必会出第一套题，加入answer[2]的集合add.(1)

# 代码实现
# -----------------------------------------------------------------------------
# 成功解决TLE,无需多次二层循环
# 注意str的join方法

n, m, k = map(int,input().split(" "))
list1 = []
for _ in range(0,n):
    list1.append(list(map(int, input().split(" "))))

answer = [set() for _ in range(k)]

for person in range(n):
    for index in range(m): 
        answer[list1[person][index] - 1].add(index)# 借助集合特性，遍历每一个人：A第二天做第一套，则在第二天必会出第一套题，加入answer[2]的集合add.(1)

results = [len(answer[ind]) for ind in range(k)]
print(" ".join(map(str, results)))

## 超时做法
# def check(need):
#     count = 0
#     for lie in range(m):
#         for hang in range(n):
#             if int(list1[hang][lie]) == need:
#                 count += 1
#                 break
#     return count

# results = [check(day + 1) for day in range(k)]
# print(" ".join(map(str, results)))


