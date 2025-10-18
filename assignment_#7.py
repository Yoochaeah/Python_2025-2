# 과제 11 - 1
a = input('숫자 5개를 입력: ').split()
print(a)

# 과제 11 - 2
a = input('숫자 5개를 입력: ').split()
b = input('문자 1개 입력: ')
a.append(b)

print(a)

# 과제 12
a = input('숫자 5개 입력: ').split()
del a[-1], a[-2]
print(a)

# 과제 13
a = input('숫자 5개 입력: ').split()
for index, value in enumerate(a, start = 101):
    print(index, value)
    
# 과제 14
a = [10, 20, 30, 40, 30, 20, 10]
result = a.count(20)

print(result)

# 과제 15
a = list(map(int, input('숫자 10개 입력: ').split()))

min_value = min(a)
max_value = max(a)

print(min_value, max_value)

# 과제 16
a = list(map(int, input('숫자 10개 입력:').split()))
result = sum(a) - max(a) - min(a)

print(result)

# 과제 17
a = [10, 20, 30, 40, 20, 10]
a = [ i for i in a if i != 20]

print(a)

# 과제 18
a = [i for i in range(1, 6)]
print(a)

# 과제 19
a = [i for i in range(1, 21) if i % 2 != 0]
print(a)

# 과제 20
a = int(input('1부터 10까지 임의의 숫자 입력: '))
b = int(input('10부터 20까지 임의의 숫자 입력: '))

c = [2 ** i for i in range(a, b+1)]

del c[-1], c[-2]

print(c)
