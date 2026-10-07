s="  KodNest Technologies 123  "
print("original string:",s)

#case conversion
print("upper():",s.upper())
print("lower():",s.lower())
print("captalize():",s.capitalize())
print("title():", s.title())
print("swapcase()",s.swapcase())

#searching and counting

print("find('Tech'):",s.find("Tech"))
print("count(0):",s.count("o"))

# replace
print("replace('123','2026'):",s.replace("123","2026"))

#start and end check
print("startswith(' kod'):", s.startswith(" kod"))
print("endswith('123  '):", s.endswith("123  "))

#split and join

words=s.split()
print("split():",words)
print("join():", "-".join(words))

# strip spaces
print("strip():",s.strip())
print("ltrip():",s.lstrip())
print("rtrip():",s.rstrip())

# checking method
print("isalpha():",s.isalpha())
print("isdigit():",s.isdigit())
print("isspace():",s.isspace())
print("isalpha():",s.isalpha())

#length
print("length of string:", len(s))