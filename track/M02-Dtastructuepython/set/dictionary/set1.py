set1={1,2,3,4,5}
set2={5,6,7,8,4,}
print(set1 | set2)
print(set1.union(set2))
print(set1 &set2)
print(set1.intersection(set2))

print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))


print(set1.difference(set2))
print(set1-set2)
print(set2-set1)
print(set1.symmetric_difference(set2))
print(set1^set2)

set1.add(9)
print(set1)

set1.update(set2)
print(set1)

# set1.remove(5)
 # print(set1)

set1.discard(5)
print(set1)

set1.pop()
print(set1)