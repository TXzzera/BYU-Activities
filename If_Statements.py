#price = input('how much did you pay? ')
#price = float(price)
#if price >= 1.00:
#    tax = .07
#else:   
#    tax = 0
#print('Tax rate is: ' + str(tax))

#country = input('What country do you live in? ')

#if country.lower() == 'canada':
#    province = input('What province do you live in? ')
 #   if province.lower() in ('alberta','nunavut','yukon'):
 #       tax = 0.05
#    elif province.lower() == 'ontario':
#        tax = 0.13
#    else:
#        tax = 0.15
#else:
#    tax = 0.00
#print(tax)

First_number = int(input('What is the first number? '))
Second_number = int(input('What is the second number? '))

if First_number > Second_number:
    print('The first number is greater')
else:
    print('The first number is not greater')

if First_number == Second_number:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if Second_number > First_number:
    print('The second number is greater')
else:
    print('The second is not greater')
print()
favorite_animal = input('What is your favorite animal? ')
if favorite_animal.lower() == 'dog':
    print('That is my favorite animal too')
else:
    print('That one is not my favorite')