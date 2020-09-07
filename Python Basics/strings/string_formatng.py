
first_name = input('Please enter your frst name :- ')
second_name = input('Please enter your second name :- ')

print()
final_name = 'hello ' + first_name + ' ' + second_name
print(final_name)
final_name = 'hello, {} {} '.format(first_name, second_name)
print(final_name)
final_name = 'hello, {0} {1} '.format(first_name, second_name)
print(final_name)
final_name = 'hello, {1} {0} '.format(first_name, second_name)
print(final_name)
print()


