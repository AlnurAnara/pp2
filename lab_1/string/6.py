'''
Slicing Strings 切片字符串
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
 The first character has index 0.
一般右括号的index不包括. e.g. [2:5]means from index 2 to 4
'''
b = "Hello, World!"
print(b[2:5]) #output: llo
print(b[:5]) #Get the characters from the start to position 5 (not included)
             #outut:Hello
print(b[2:]) #Get the characters from position 2, and all the way to the end
             #llo, World!

print(b[-5:-2])#Use negative indexes to start the slice from the end of the string
               # output: orl
'''
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
'''