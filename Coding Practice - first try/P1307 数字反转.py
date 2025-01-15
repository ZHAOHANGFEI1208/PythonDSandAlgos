user_input = input()

def my_reverse(s):
    list1 = list(s)
    list1.reverse()
    while list1[0] == "0":
        list1.pop(0) 
    new_s = "".join(list1)
    return new_s

if user_input[0] == "-":
    user_input = list(user_input[1:])
    s = my_reverse(user_input)
    print(f"-{s}")
elif user_input == "0":
    print(0)
else:
    s = my_reverse(user_input)
    print(s) 
