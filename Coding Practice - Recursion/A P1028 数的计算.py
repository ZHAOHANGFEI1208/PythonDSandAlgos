## 代码实现
# 加入缓存思想memo

# count = 1
# def func(list1:list):
#     global count
#     if list1[len(list1)- 1] <= 1:
#         return 
#     for num in range(1, round((list1[len(list1) - 1]) / 2) + 1):
#         if num <= list1[len(list1) - 1] / 2:
#             list1.append(num)
#             count += 1
#             func(list1)
#             list1.pop()

# list1 = int(input())
# list1 = [list1]
# func(list1)
# print(count)


    
memo = {}
def count_sequences(num:int, memo:dict):
    if num in memo:
        return memo[num]
    
    if num <= 1:
        return 1
    
    count = 1
    for num1 in range(1, (num//2)+1):
        count += count_sequences(num1, memo)
    
    memo[num] = count
    return count

num = int(input())

result = count_sequences(num,memo)
print(result)
    
        

