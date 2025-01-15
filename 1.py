def count_sequences(n, memo={}):
    # 检查是否已经计算过
    if n in memo:
        print(f"使用缓存结果，n={n}，结果={memo[n]}")
        return memo[n]
    
    # 递归终止条件：当n为1时，只有一个数列
    if n == 1:
        print(f"基础情况：n={n}，计数=1")
        return 1
    
    # 递归计算：n可以独立成一个数列，加上所有以n结尾的数列
    count = 1  # n本身可以独立成一个数列
    print(f"开始递归调用，n={n}")
    for i in range(1, n // 2 + 1):
        print(f"递归调用，n={n}，i={i}")
        count += count_sequences(i, memo)
    
    # 存储结果
    memo[n] = count
    print(f"缓存结果，n={n}，结果={count}")
    return count

# 读取输入
n = int(input().strip())

# 计算并输出结果
result = count_sequences(n)
print(f"n={n}的合法数列总数：{result}")