# 代码实现
# -----------------------------------------------------------------------------
# 1. 注意list（）方法的使用：list1 = list(map(int, input().split(" ")))
# 2. 回顾一下：reverse()的返回值是bool类型，返回是否完成反转；只要调用即完成反转

list1 = list(map(int, input().split(" ")))
list1.pop()
list1.reverse()
for index in range(len(list1)):
    if index == len(list1) - 1:
        print(list1[index])
    else:
        print(list1[index], end=" ")
    
