#strings are also sequences, just like lists, but of characters
fav_colour = 'Green'
print(fav_colour[3])
print(fav_colour[:6])

#other modifiers for string

text = 'this is lower case'
text_cap = text.upper()
print(text_cap)

user_number = input ('Please enter a number: ')
if user_number.isnumeric():
    print('Thanks!')
else:
    print('This is not a number')
    
#.upper and .lower change text strings. can use islower and isspace as well. isnumeric checks if the string is only a numeric figure
