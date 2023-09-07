# thise code checks if the input is part of the government_departments list and depending on it prints a specified message in response
government_departments = ['Cabinet Office', 'HM Treasury', 'Home Office', 'Ministry of Defence', 'Ministry of Justice']
employer = input('Where do you work? ')
if employer in government_departments:
    print('You may enter the building')
else: 
    print('Security Alert!')
# we can do the same in reverse
government_departments = ['Cabinet Office', 'HM Treasury', 'Home Office', 'Ministry of Defence', 'Ministry of Justice']
employer = input('Where do you work? ')
if employer not in government_departments:
    print('Security Alert!')
else: 
    print('Please enter!')
