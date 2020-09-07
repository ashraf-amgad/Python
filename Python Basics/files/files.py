#open file
file_read = open("file.txt" , 'r')

#return string 
#lines = file1_read.read()

#return list 
lines = file_read.readlines()
print('this is the lines\' list: ')
print(lines)


for search_word in lines:
    if(search_word == 'Ashraf'):
        print('\n Ashraf word is found in a line and this the word ' + search_word + '\n')

file_read.close()


html_file_write = open("file.html" , 'w')

html_file_write.write("this is a html file")

html_file_write.close()


