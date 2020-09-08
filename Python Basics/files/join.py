#open file
file_read = open("file.txt" , 'r')

#return string 
#lines = file1_read.read()

#return list 
lines = file_read.readlines()
#print('this is the lines\' list: ')
#print(lines)


# add ' ' space between each element in a list 
print('\nthis is the lines\' string with join : ')
temp = ' '.join(lines) 
print('temp_type is : ' + str(type(temp)) + ' and content is : ' + temp )



file_read.close()


