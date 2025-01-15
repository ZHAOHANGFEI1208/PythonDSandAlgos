user_input = input()
parts = user_input.split()
n = int(parts[0])
x = int(parts[1])
times = 0

for i in range(1, n + 1):
    num = i
    while num > 0:
        digit = num % 10
        if digit == x:
            times += 1
        num //= 10

print(times)