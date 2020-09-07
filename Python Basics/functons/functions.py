



print()

def add_print_fun(task_name, number):
    print(task_name, 'is done addition is ', number)

def add(first_number, second_number):
    return (first_number + second_number)


add_print_fun('first task', add(12,10))

# it's better to deal with name notation when you call a function
# it's more readable 
add_print_fun(number= add(5,7), task_name = 'second task')
add_print_fun(number= add(3,0), task_name = 'third task')


print()






