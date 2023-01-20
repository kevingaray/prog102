## Dictionary
my_dict = {} 
my_dict = dict()

person = {'name': 'Gramsci', 'last_name': 'Hermozo', 0:'two'}
# print(person['name'])
last_name = person.get('last', 'this person dont have property') # .get() no devuelve error sino 'None'
# print(last_name)
# print(person[0])

# print(person.keys())
# print(person.values())

# for item in person:
#     print(item) # only print keys

# for key,value in person.items():
#     print(key,value,sep=" : ")

## Set
my_set = set()
my_set.add(1)
my_set.add(4)
my_set.add('nombre')
my_set.remove(1)
print(my_set)