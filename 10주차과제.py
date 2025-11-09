# 과제 25
keys = input("키 입력: ").split()
values = [int(v) for v in input("값 입력: ").split()]
result = dict(zip(keys, values))

print(result)

# 과제 26
park = { 'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
print(park['english'])
print(park['science'])

# 과제 27
kim = { 'korean': 94, 'english': 91, 'mathematics' : 89, 'science': 83}
for subject in kim.keys():
    kim[subject] = 100
print(kim)

# 과제 28
lee = { 'korean': 94, 'english': 91, 'mathematics': 89, 'science' : 83}
if 'english' in lee:
    del lee['english']
print(lee)

# 과제 29
lim = { 'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
for key, value in lim.items():
    print(key, value)

# 과제 30
choi = { 'korean' : 94, 'english': 91, 'mathematics': 89, 'science': 83}
high_scores_dict = {key: value for key, value in choi.items() if value >= 90}
print(list(high_scores_dict.keys()))

# 과제 31
yoo = { 'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum(yoo.values()) / len(yoo)
print(average)
