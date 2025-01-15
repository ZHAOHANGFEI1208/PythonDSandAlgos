# 代码实现
# -----------------------------------------------------------------------------
# 1.给数组（list实现）赋值
# 使用切片操作 以及注意引用对象：list1[start:end+1] = [-1] * (end - start + 1)
# 突然发现用列表生产式合理一点：list1:list[0:length] = [1 for _ in range(length+1)]
length, account = map(int, input().split())
list1:list[0:length] = [1 for _ in range(length+1)]
for _ in range(account):
    start, end = map(int, input().split())
    list1[start:end+1] = [-1] * (end - start + 1)
print(list1.count(1))

