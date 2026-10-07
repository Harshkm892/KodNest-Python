#sets are unordered, unindexed and mutable unchangable
#do not support duplicate value

s={1,2,3,4,5}
print(s,type(s))

s.add(6)
s.update({8,9})
s.discard(10)
s.pop()
s.pop()
# s.clear()

# del s

print(s)

s1={1,2,3,"hello!",1.2,True,0,1.234,False }
print("s1:",s1)

#constructor set
s2=set()
print(s2,type(s2)) #empty set
s3=set([1,2,3,4])
print("s3:",s3,type(s3))

for n in s3:
    print(n)

    #Immutable-frozenset
    fs=frozenset([1,2,3])
    print(fs,type(fs))
    fs.add(6)
print(fs)