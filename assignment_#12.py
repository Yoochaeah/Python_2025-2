# 32
fav1 = {1, 2, 3, 4, 5}
fav2 = {1, 3, 5, 7, 9}

uni = set.union(fav1, fav2)
intersec = set.intersection(fav1, fav2)

print(uni, intersec)

# 33
fav1 = {2, 4, 6, 8, 10}
fav2 = {1, 2, 3, 4, 5}

diff = set.difference(fav1, fav2)
symdiff = set.symmetric_difference(fav1, fav2)

print(diff, symdiff)

# 34
fav = {1, 2, 3, 4, 5}
fav.update( {100} )

print(fav)

# 35 - 1
a = {100, 200, 300, 400, 500}
a.intersection_update( {400, 500, 600, 700, 800} )

print(a)

# 35 - 2
a = {100, 200, 300, 400, 500}
a.difference_update( {400, 500, 600, 700, 800} )

print(a)

# 35 - 3
a = {100, 200, 300, 400, 500}
a.symmetric_difference_update( {400, 500, 600, 700, 800} )

print(a)

# 36
a = {100, 200, 300, 400, 500}

if (a <= {100, 200, 300, 400, 500}):
    print('부분')
if a > {100, 200, 300, 400, 500}:
    print('상위')
if a >= {100, 200, 300, 400, 500}:
    print('동시')
    
# 37
fav = {1, 2, 3, 4, 5}
fav.add(1000)
fav.discard(1000)
print(fav)

# 38
multiples = {x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0}
print(multiples)