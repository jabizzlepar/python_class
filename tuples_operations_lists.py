#list uses [] and tuple uses ()

empty_tuple = ()
one_element_tuple = 1, #need to add the , to make it clear that we are not just assigning a single variable

#considering the above the , is not necessary if more than one element is provided

two_element_tuple = 1,2

print(two_element_tuple)

#mutable vs immutable data! A tuple is immutable. We can reassign a tuple with new variables, but we cannot modify an existing tuple with new element. It would just be replaced.
user_data = ('John', 'American', 1072)
print(len(user_data))
if 'American' in user_data:
    print('He is american!')
for element in user_data:
    print(element)

#we can also add tuples
user_data = ('John', 'American', 1072)+ ('Mary','German', 1928)
print(user_data)
#note that this does not append the existing tuple. We overwrite the variable user_data with a newly created tuple instead.
#when to use what?
#list = many values of the same data type etc. 
#tuples = many values of different data types 

#we can also have tuples as list elements and lists as elements of a tuple

city_1 = ('London','UK', 9000000)
city_2 = ('Berlin','Germany', 3000000)
city_3 = ('Phoenix','USA', 6000000)

cities = [('London','UK', 9000000), ('Berlin','Germany', 3000000), ('Phoenix','USA', 6000000)]

for city in cities:
    print('Name:', city[0], ', Country:', city[1], ', Population:', city[2])


#now lets do list within tuples
user_data = ('Jasper','German', 1998, [68.0,70.1,68.5])
user_data[3].append(71.1)
print(user_data)
#so if a tuple includes a list, the list remains being mutable if we target it with [] 
