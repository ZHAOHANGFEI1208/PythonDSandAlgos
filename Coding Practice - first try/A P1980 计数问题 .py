# 代码实现
# -----------------------------------------------------------------------------
# input().split(" ")的妙用；
# 转字符串，再转列表，使用extend()和count()完成计数

n,x=input().split(" ")
n=int(n)
l=[]
for i in range(1,n+1):
    l.extend(list(str(i)))
print(l.count(x))