# 39
def print_odds(n):
    for i in range(0, n + 1):
        if i % 2 == 1:
            print(i)
num = int(input('정수 입력: '))
print_odds(num)

# 40
def print_three(n):
    for i in range(0, n + 1):
        if i % 3 == 0:
            print(i)
num = int(input('정수 입력: '))
print_three(num)

# 41
def print_maxmin(nums):
    return max(nums), min(nums)
nums = list(map(int, input('숫자 4개 입력: ').split()))

# 42
def print_odds(n):
    for i in range(0, n + 1):
        if i % 2 == 1:
            print(i)
num = int(input('정수 입력: '))
print_odds(num)

# 43
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n = int(input('0보다 크거나 같은 정수 입력: '))
print(factorial(n))

# 44
def product_sum(start_i, end_i, start_j, end_j):
    total_sum = 0
    for i in range(start_i, end_i + 1):
        for j in range(start_j, end_j + 1):
            if i * j >= 30:
                total_sum += (i + j)
    return total_sum
result = product_sum(2, 9, 2, 9)
print(result)

# 45
def  cul_sum(a):
    result_list = []
    total = 0

    for num in a:
        total += num
        result_list.append(total)
        
    return total

a = [1, 2, 3, 4, 5]
print(cul_sum(a))