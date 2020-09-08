#open file
file_name = 'file.txt'
file_read = open(file_name , 'r')


file_content = file_read.read()

#return list with file's lines
file_lines = file_content.split('\n')
#print(file_lines)

line_number = 0
word_number = 0
#return list with each word in the file's lines
for _file_line_ in file_lines:
    line_number += 1
    file_words = _file_line_.split(' ')
    #print(file_words)
    for _file_word_ in file_words:
        word_number += 1
        if (_file_word_ == 'Ashraf'):
            print('I found Ashraf word in \"' + file_name\
                   + '\" in line ' + str(line_number)\
                       + ' and word column number ' + str(word_number))
    
    word_number = 0 



file_read.close()




