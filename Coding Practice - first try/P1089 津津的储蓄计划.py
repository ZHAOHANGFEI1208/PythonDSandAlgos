# 换行输出案例
parts = []
for _ in range(12):
    parts.append(int(input()))

now_month = 1
now_money = 0
mom = 0
need2break = 0
for x in parts:
    now_money = now_money + 300 - x
    if now_money >= 100:
        while now_money >= 100:
            now_money -= 100
            mom += 100
    elif now_money < 0:
        need2break = 1
        print(f"-{now_month}")
        break
    now_month += 1

if need2break == 0:
    print(int(now_money + mom*1.2))


        


