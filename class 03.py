# # List
# my_list = []
# my_list = list()
# names = ['jose','Jaime','Karla',12]
# print(names[0].title())
# print(names[-1])

# Changind and adding
motorcycles = ['honda','yamaha','suzuki']
motorcycles[0] = 'ducati'
motorcycles.append('bmw')
motorcycles.insert(1,'ktm')
# print(motorcycles)

# removing
# del motorcycles[0] # si no se coloca el indice , va a eliminar la variable
# motorcycles.remove('suzuki')
# print(motorcycles)

# ordenando
# motorcycles.sort() # modifica la lista original
# print(motorcycles)
# print(sorted(motorcycles)) # no modifica la lista original

## iteration list
# for motorcycle in motorcycles:
#     print(motorcycle)

# for index in range(0,len(motorcycles)):
#     print(motorcycles[index])

## comprenhension list
upper_list = [item.upper() for item in motorcycles if item != "bmw"]
# print(upper_list)

# Tuple
tpl = ()
tpl = tuple() # es inmutable por eso es raro definirlo asi
tpl = ('elem1','elem2','elem3')

# print(*motorcycles[2:4])

############################################################
# File Reader
file = open('text_for_class_03.txt')
print(file.read())

# with open('text_for_class_03.txt') as file:
#     for 
