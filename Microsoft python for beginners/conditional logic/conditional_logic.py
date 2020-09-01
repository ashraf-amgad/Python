


first_number = input('please enter your first number: ')
second_number = input('please enter your second number: ')


if float(first_number) == float(second_number):
    print('\nequal.')
else:
    print('\nnot equal!')


name = 'ASHRAF'

if name == 'ashraf':
    print('if statement is not a case senstive')
else:
    print('if statement is a case senstive')

if name.lower() == 'ashraf':
    print('pass with lower function\n')
else:
    print("doesn't pass with lower function\n")


letter = input('please enter a letter : ')
if letter == 'A' \
   or letter.lower() == 'a':
    print('yes excellent \n')
elif letter in ('b', 'B', 'c', 'C'):
    print("very good or Good \n")
else:
    print('pass \n')







