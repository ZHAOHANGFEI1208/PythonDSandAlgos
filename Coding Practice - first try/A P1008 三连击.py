# 只存在123456789处理 -- set
def check(a, b, c):
    digits = set(str(a) + str(b) + str(c))
    return len(digits) == 9 and all(digit in digits for digit in "123456789")
for a in range(100,330):
    b = 2 * a
    c = 3 * a
    if check(a, b, c):
        print(f"{a} {b} {c}")
