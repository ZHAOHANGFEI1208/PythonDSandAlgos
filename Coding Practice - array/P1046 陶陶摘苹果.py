user_input = input()
apples = map(int,user_input.split())
user_input2 = input()
height = int(user_input2)
num = 0
for apple in apples:
    if height + 30 >= apple:
        num += 1
print(num)