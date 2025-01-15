# 代码实现
# -----------------------------------------------------------------------------
# map的运用：
# a,b=map(int,input().split())
# print(a+b)

user_input = input()
parts = user_input.split()
sum:int = 0
for item in parts:
    sum += int(item)
print(sum)

