left = 1
right = 1
number = 1
turn = 1
need = int(input())
end = 0
max_num = 1
while 1:
    if end == 1:
        break
    elif need == 1:
        print(f"1/1")
        break 
    if turn % 2 == 1:
        max_num += 1
        number += 1
        right = max_num
        left = 1
        if need == number:
            print(f"{left}/{right}")
            end = 1
        while left != max_num:
            number += 1
            right -= 1
            left += 1
            if need == number:
                print(f"{left}/{right}")
                end = 1
                break
        turn += 1
    else:
        max_num += 1
        number += 1
        left = max_num
        right = 1
        if need == number:
            print(f"{left}/{right}")
            end = 1
        while right != max_num:
            number += 1
            left -= 1
            right += 1
            if need == number:
                print(f"{left}/{right}")
                end = 1
                break
        turn += 1





        






