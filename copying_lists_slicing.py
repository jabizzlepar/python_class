data_original = [3,4,6]
data_new = data_original
data_original[0] = 32
print('Original', data_original, '\nNew:', data_new)
# here modifying the new list also modifies the original list
# this is because with complex data-types like lists, the name of the list does not actually point to the actual list. Instead, the name of the list points to the name of the location of the list. 
# that is why the modification of the list affects the new list, as they actually share the very same list 
# how can we then actually make a copy?

# use slicing instead
data_original = [3,4,6]
data_new = data_original[:] # remember!! [:]
data_original[0] = 32
print('Original', data_original, '\nNew:', data_new)
