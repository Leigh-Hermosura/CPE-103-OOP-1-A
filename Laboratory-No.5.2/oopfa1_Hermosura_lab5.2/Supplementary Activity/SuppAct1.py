# 1.	Create a SURNAME.txt to file write your analysis in the text file.
# Write a program to read through a file and print the contents of the file (line by line).

file = open('../HERMOSURA.txt', encoding='utf-8')
for line in file:
    line = line.rstrip()
    print(line)
