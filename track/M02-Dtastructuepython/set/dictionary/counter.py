language=["python","java","python","c++","java","c++"]
frequency={}
for lan in language:
    if lan in frequency:
        frequency[lan]+=1
    else:
        frequency[lan]=1
print(frequency) 



#using counter


