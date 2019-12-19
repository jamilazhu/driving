country = input('Which country are you from : ')
age = input('Please enter your age : ')
age = int(age)
if country == 'China':
    if age >= 18:
        print('You can conduct the test')
    else:
        print('You can not yet conduct the test')
elif country == 'USA':
    if age >= 16:
        print('You can conduct the test')
    else:
        print('You can not yet conduct the test')
else: 
    print( 'Wrong input, only China or USA')

