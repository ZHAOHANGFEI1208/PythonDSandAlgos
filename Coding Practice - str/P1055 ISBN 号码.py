user_input = input()

wait2check_number = user_input[len(user_input) - 1]

str1 = user_input[0:(len(user_input)-2)]

str2 = str1.split("-")
str2 = "".join(str2)
sum = 0
for ind in range(len(str2)):
    sum += int(str2[ind]) * (ind + 1)
 
right_number = str(sum % 11)
if right_number == "10":
    right_number = "X"
if right_number == wait2check_number:
    print("Right")
else:
    print(f"{str2[0]}-{str2[1:4]}-{str2[4:9]}-{right_number}")