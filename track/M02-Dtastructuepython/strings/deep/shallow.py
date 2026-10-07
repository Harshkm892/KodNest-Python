a=[10,20,30,40]
print("original a",a)
b=a
a[2]=300
print(a)
print(b)

a1=[10,20,30,40]
b1=a1.copy()
b1[2]=300
print(a1)
print(b1)

c1=[4,5,6,7,8]
d1=c1[:]
d1[2]=800
d1.pop()
print(c1)
print(d1)
