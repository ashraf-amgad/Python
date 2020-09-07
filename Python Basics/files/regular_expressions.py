
import re

file1_write = open("file1.txt" , 'a')
#file1_write.write("Ashraf")
file1_write.close()


file1_read = open("file1.txt" , 'r')
for line in file1_read:
    if re.search("(As|He)" , line):
        print(line)

file1_read.close()