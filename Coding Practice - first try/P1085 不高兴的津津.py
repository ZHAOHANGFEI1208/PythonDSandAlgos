time = 0
max_number = -999 
for now_day in range(1,8):
    user_input = input()
    parts = [int(x) for x in user_input.split()]
    now_day_number = parts[0] + parts[1]
    if now_day_number > 8 and now_day_number > max_number :
        max_number = now_day_number
        time = now_day
print(time)