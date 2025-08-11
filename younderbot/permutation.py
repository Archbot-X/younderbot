import itertools
num=[1,1,2]

perm=itertools.permutations(num)

all_perm=set(perm)
print("The iteration is: ")
for perm in all_perm:
    print(*perm)