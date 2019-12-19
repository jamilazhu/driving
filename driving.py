country = input('Which country are you from : ')
age = input(' Please enter your age : ')
age = int(age)
if country == 'China':
    if age >= 18:
        print('you can conduct the test')
    else:
        print('you can not yet conduct the test')

        
