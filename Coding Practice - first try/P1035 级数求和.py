k = int(input())
x = 1
S_n = 0
while 1:
    S_n += 1 / x
    if S_n > k:
        print(x)
        break
    x += 1

        