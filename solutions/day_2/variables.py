
## Day 2: 30 days of Python programming.

# Exercises: Level 1
firstName = 'Juani'
lastName = 'Schegtel'
fullName = firstName + ' ' + lastName
country = 'Argentina'
city = 'Goya'
age = 25
year = 2025
isMarried = False
isTrue = True 
isLightOn = False
delantero, mediocampista, defensor = 'Borja', 'El Pity', 'Paulo Díaz'

# Exercises: Level 2
print("Variable 1: ", type(firstName))
print("Variable 2: ", type(lastName))
print("Variable 3: ", type(fullName))
print("Variable 4: ", type(country))
print("Variable 5: ", type(city))
print("Variable 6: ", type(age))
print("Variable 7: ", type(year))
print("Variable 8: ", type(isMarried))
print("Variable 9: ", type(isTrue))
print("Variable 10: ", type(isLightOn))
print("Variable 11: ", type(delantero))
print("Variable 12: ", type(mediocampista))
print("Variable 11: ", type(defensor))

firstNameLen = len(firstName)
lastNameLen = len(lastName)

print(f'La longitud del primer nombre es: { firstNameLen }')
print(f'La longitud del segundo nombre es: { lastNameLen }')

if firstNameLen > lastNameLen:
    print('El primer nombre es más largo que el segundo.')
elif firstNameLen < lastNameLen:
    print('El segundo nombre es más largo que el primero.')
else:
    print('Los nombres tienen la misma longitud.')

num_one, num_two = 5, 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(f'Total = {total}')
print(f'Difference = {diff}')
print(f'Product = {product}')
print(f'Division = {division}')
print(f'Remainder = {remainder}')
print(f'Exponential = {exp}')
print(f'Floor Division = {floor_division}')

import math 
radius = 30
pi = math.pi
area_of_circle = pi * radius ** 2 
circum_of_circle = pi * radius
print('The radius of a circle is 30m:')
print(f"It's area is {area_of_circle:.4f} and the circumference {circum_of_circle:.4f}")
radius = int(input('Enter a value for the radius of the circle: '))
area_of_circle = pi * radius ** 2 
circum_of_circle = pi * radius
print(f"It's area is {area_of_circle:.4f} and the circumference {circum_of_circle:.4f}")

print('\nI want to know about you... ')
names = input('Tell me your first and last name (separated by a blank space): ')
firstName, lastName = names.split()
country = input('Now, your country of birth: ')
age = input('And the last thing to know about you is your age: ')
print(f'So, you are {firstName} {lastName} born in {country} and you are {age} years old.')

