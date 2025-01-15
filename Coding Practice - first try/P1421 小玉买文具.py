# 同一行输出案例
user_input = input()
parts = user_input.split()
sum = int(parts[0]) * 10 + int(parts[1])
print(sum // 19)