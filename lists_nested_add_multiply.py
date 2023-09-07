numbers = [1,2,3,4]
countries = ['UK','USA','Germany']

#this is a nested list
cells = [['A1','A2','A3'], ['B1','B2','B3']]
cells[0]

for x in cells:
    print('Element:', x)
    #this will only print the lists themselves and not the individual elements within them

# so instead we have to use a nested for loop as well
cells = [['A1','A2','A3'], ['B1','B2','B3']]
for x in cells:
    for y in x:
        print('Element', y)

  #lets print this in the form of a table instead

# so instead we have to use a nested for loop as well
cells = [['A1','A2','A3'], ['B1','B2','B3']]
for x in cells:
    for y in x:
        print(y, '', end='')
    print()

#lets make a table using range 
table = [[i for i in range (1,6)] for j in range(4)]

# lets add lists together
list_uk =['London', 'Manchester']
list_us = ['NY','LA']
list_all = list_uk+list_us
print(list_all)

# lets repeat the list
list_numbers = [0,1,2]*10
print (list_numbers)
