# 算法流程：

# 小写所有字母
# 单词和文章前后各加一个空格然后找到位置
# (1)如果位置返回-1(说明没有)那么就输出-1
# (2)否则就逐个比较单词统计个数

# 代码实现：

# find的使用 format的使用

key = input().lower()
passport = input().lower()

list1 = passport.split()

firstfindindex = " {} ".format(passport).find(" {} ".format(key))

cnt = 0
if firstfindindex == -1:
    print(-1)
else:
    for word in list1:
        if word == key:
            cnt += 1
    print(f"{cnt} {firstfindindex}")

    