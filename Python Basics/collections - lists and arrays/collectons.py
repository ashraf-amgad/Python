

from array import array

print()

names = ['ashraf']
names.insert(1, 'khaled')
print('number os items', len(names))
print(names)

ages = []
ages.append (25)
ages.append (23)
print(names[0], ages[0])
print(names[1], ages[1])
print()


# dectionary 
ashraf_name = {'first': 'ashraf', 'second': 'amgad'}
khaled_name = {}
khaled_name['first'] = 'khaled'
khaled_name['second'] = 'amgad' 

# list of dectionaries, lists, arrays, strings, numbers ....
names = []
names.append(ashraf_name)
names.append(khaled_name) 
print(names, '\n')
print(names[0]['first'], '\n')
