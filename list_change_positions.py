first = input('Enter the first number: ')
second = input('Enter the second number: ')

# first = second -- here the first input variable is lost when we just swap as such. Not a viable solution
# can we use a temporary variable that we dump as an empty one?

#temporary = first
#first = second
#second = temporary

# there is apparently a better shortcut

print('Prior to swap:', first, second)
first, second = second, first
print('After swap:', first, second)

# the swap shortcut also works for lists

london_borough = ['Westminister', 'Hillingdon', 'Hounslow', 'Camden', 'Ealing', 'Hackney', 'City of London', 'Bromley']

# lets swap the order of those boroughs
print('Prior to swap:', london_borough)
london_borough[0], london_borough[1] = london_borough[1], london_borough[0]
print('After swap:', london_borough)

# sorting a list array alphabetically
london_borough = ['Westminister', 'Hillingdon', 'Hounslow', 'Camden', 'Ealing', 'Hackney', 'City of London', 'Bromley']
london_borough.sort()
print(london_borough)

# we can also sort numbers 
numbers = [2,6,1,2,0,-5]
numbers.sort()
print(numbers)

#or reverse it
random_numbers = [7,6,2,34,8,-1,-5,-2]
random_numbers.sort(reverse=True)
print(random_numbers)


# these are methods so cannot undo the sort easily.

# to avoid forever sorting it, just use sorted instead -- sort vs. sorted
london_borough = ['Westminister', 'Hillingdon', 'Hounslow', 'Camden', 'Ealing', 'Hackney', 'City of London', 'Bromley']
print(sorted(london_borough))
print(london_borough)

# sort is a method that works on the list itself - sorted is a general purpose function that doesn't change the actual list
