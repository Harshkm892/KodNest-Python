
# string[start:stop:step]


# LEVEL 1 - BASIC start:stop



# 1. Extract the first 3 characters

text = "Python"

print(text[0:3])
# pyt



text = "Programming"

print(text[1:5]) #rogr



text = "Developer"

print(text[2:6]) #velo





# 4. Extract characters from index 3 to 6

text = "Computer"

print(text[3:7]) #pute





# 5. Extract the first 4 characters

text = "Artificial"

print(text[0:4]) #Arti




# 6. Extract characters from index 2 to 6

text = "Education"

print(text[2:7]) #ucati





# 7. Extract characters from index 4 to 9

text = "JavaScript"

print(text[4:10]) #script





# 8. Extract characters from index 4 to 9

text = "DataScience"

print(text[4:10]) #Scienc





# ------------------------------------------------------------

# LEVEL 2 - MISSING START OR STOP

# ------------------------------------------------------------



# 9. Extract from beginning to index 5

text = "PythonProgramming"

print(text[:6]) # python





# 10. Extract from index 6 to the end

text = "PythonProgramming"

print(text[6:]) #programming





# 11. Extract from beginning to index 8

text = "FullStackDeveloper"

print(text[:9]) #fullstack





# 12. Extract from index 9 to the end

text = "FullStackDeveloper"

print(text[9:]) #developer





# 13. Extract from beginning to index 6

text = "MachineLearning"

print(text[:7]) #Machine





# 14. Extract from index 7 to the end

text = "MachineLearning"

print(text[7:]) #learning





# ------------------------------------------------------------

# LEVEL 3 - POSITIVE STEP

# ------------------------------------------------------------



# 15. Take every second character

text = "ABCDEFGHIJ"

print(text[0:8:2]) # aceg





# 16. Take every second character

text = "ABCDEFGHIJ"

print(text[1:9:2]) #BDFH





# 17. Take every third character

text = "ABCDEFGHIJKL"

print(text[0:12:3]) #ADGJ


text = "ABCDEFGHIJKL"

print(text[2:10:2])
#cegi

# 19. Take every second number

text = "1234567890"

print(text[0:10:2]) #2468


# 20. Take every second number starting from index 1

text = "1234567890"

print(text[1:9:2]) #3579





# ------------------------------------------------------------

# LEVEL 4 - TRICKY POSITIVE SLICING

# ------------------------------------------------------------



# 21. Take every third character

text = "Programming"

print(text[0:11:3]) #pgmr





# 22. Take every third character starting from index 1

text = "Programming"

print(text[1:10:3]) # oam




text = "PythonProgramming"

print(text[2:14:2]) #tto


# 24. Take every third character

text = "PythonProgramming"

print(text[1:15:3]) #oyhmg





# 25. Take every second character

text = "ABCDEFGHIJKLMNO"

print(text[3:13:2]) #dhj





# 26. Take every third character

text = "ABCDEFGHIJKLMNO"

print(text[2:14:3]) #cegi





# ------------------------------------------------------------

# LEVEL 5 - INTERVIEW STYLE

# ------------------------------------------------------------



# 27. Predict the output

text = "PythonProgramming"

print(text[0:16:4])  #pto





# 28. Predict the output

text = "ABCDEFGHIJKLM"

print(text[1:12:3]) #beg





# 29. Predict the output

text = "DataScienceWithPython" 

print(text[4:18:2]) # sineihy
 




# 30. Predict the output

text = "FullStackDevelopment" 

print(text[2:19:3]) #ltkvoe





# ------------------------------------------------------------

# CONCEPT QUESTIONS

# ------------------------------------------------------------



# 31. Compare the following

text = "Python"



print(text[1:5]) #ytho

print(text[1:5:1]) #ytho

print(text[1:5:2]) #yh





# 32. What happens when start > stop?

text = "Python"

print(text[4:2]) # no print 





# 33. What happens when start == stop?

text = "Python"

print(text[2:2]) # no print





# 34. What happens when indexes are outside the string?

text = "Python"

print(text[10:20])
# no print




# 35. What happens when stop is larger than the string length?

text = "Python"

print(text[0:100])
#Python




# ------------------------------------------------------------

# BONUS CHALLENGES

# ------------------------------------------------------------



# 36. Predict the output

text = "ABCDEFGHIJKLM"

print(text[2:11:3]) #CFI





# 37. Predict the output

text = "ProgrammingLanguage"

print(text[3:15:2]) #gamnLn





# 38. Predict the output

text = "PythonDeveloper"

print(text[1:12:3]) #yoel





# 39. Predict the output

text = "DataScience"

print(text[0:10:2]) #DtSin





# 40. Predict the output

text = "FullStackDeveloper"

print(text[4:16:2]) #Sakeeo

