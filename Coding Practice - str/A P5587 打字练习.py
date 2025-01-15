## 最扯的是范文也有退格键

list1 = list()
list2 = list()
while 1:
    user_input = input()
    if user_input != "EOF":
        list1.append(user_input)
    else:
        break

while 1:
    user_input = input()
    if user_input != "EOF":
        list2.append(user_input)
    else:
        break

using_time = int(input()) / 60.0 # 分钟

# print(*list1)
# print(*list2)
# print(using_time)

## 对list2做处理: <的处理
# for row in range(len(list2)):
#     for index in range(len(list2[row])):
#         # 这里情况特殊，只需要删一个，所以删完直接break -- 错误，实际上退格键是多个的
#         if index == 0 and list2[row][index] == "<":
#             list2[row][index] = list2[row][index][1:]
#             break
#         elif index != 0 and list2[row][index] == "<":
#             list2[row] = list2[row][:index-1] + list2[row][index+1:]
#             break
for row in range(len(list2)):
    # 使用列表来存储字符，方便删除
    chars = list(list2[row])
    i = 0
    while i < len(chars):
        if chars[i] == "<":
            if i > 0:
                # 删除前一个字符和当前的退格键
                del chars[i-1]
                del chars[i-1]
                i -= 1  # 因为删除了两个字符，所以i需要减1
            else:
                # 忽略行首的退格键
                del chars[i]
        else:
            i += 1
    # 将列表转换回字符串
    list2[row] = ''.join(chars)

for row in range(len(list1)):
    # 使用列表来存储字符，方便删除
    chars = list(list1[row])
    i = 0
    while i < len(chars):
        if chars[i] == "<":
            if i > 0:
                # 删除前一个字符和当前的退格键
                del chars[i-1]
                del chars[i-1]
                i -= 1  # 因为删除了两个字符，所以i需要减1
            else:
                # 忽略行首的退格键
                del chars[i]
        else:
            i += 1
    # 将列表转换回字符串
    list1[row] = ''.join(chars)

# print(list2)
cnt = 0
## 逐行比较
for row in range(len(list1)):
    if row < len(list2): ## 贪心思想
    ## 逐字比较
        for index in range(min(len(list1[row]), len(list2[row]))):
            if list1[row][index] == list2[row][index]:
                cnt += 1
print(round(cnt / using_time))
            


