# -*- coding: utf-8 -*-

#Single string
print("What a lovely day!")
print("Naah, I am too lazy to work, let's go to pub!")
# Multiple String
print("1","2","3")
# In expression
print(print('We are learning Python!') == print("We are learning Python!"))
# Empty Line
print()

# With non default separator, default is space
print("Get","Set","Go", sep="-")
# With non-default endline separator, default is newline char
print("Hello", end=" ")
print("World")
# Print with escape
print("This is a line.\nAnd this is another line.")
print("Name:\tAnonymous")
print("Path to the folder: C:\\Users\\Anonymous")

# Print to non default stream, default is sys.stdout
import sys
print('Test error output', file = sys.stderr)

# Printing to a file
sample = open("temp.txt", 'w')
print("Print to file", file=sample)
sample.close()

# print and flush, no block buffering
print("Print and flush", flush=True)
