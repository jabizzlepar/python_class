numbers = [1,2,3,4]
#come up with an idea to make a list of 0 to 100 without writing it manually

numbers = []
for i in range (1,101):#remember that the endpoint is non-inclusive but the startpoint is
    numbers.append(i)
print(numbers)

#python apparently has a better solution
numbers = [i for i in range(1,101)]
print(numbers)

#and we can add an if statement to it as well - lets exclude numbers that are divisible by 3 i.e. modular division = 0
numbers = [i for i in range(1,101) if i%3 !=0]
print(numbers)
#it works!
