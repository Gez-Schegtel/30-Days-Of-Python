print("\n💻 Exercises: Day 9\n\nExercises: Level 1\n")

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

#       Enter your age: 30
#       You are old enough to learn to drive.
#       Output:
#       Enter your age: 15
#       You need 3 more years to learn to drive.

age = int(input("1. Ingresa tu edad: "))

# if 18 - age == 1:
#     faltante = "falta"
#     tiempo = "año"
# else:
#     faltante = "faltan"
#     tiempo = "años"

faltante, tiempo = ("falta", "año") if 18 - age == 1 else ("faltan", "años")

if age >= 18:
    print("Tenés edad suficiente para manejar.")
else:
    print(f"Te {faltante} {18 - age} {tiempo} para poder manejar.")

print()  ## Agrego un salto de línea.

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

#       Enter your age: 30
#       You are 5 years older than me.

user_age = int(input("2. Ingresa tu edad: "))
my_age = 25

age_difference = my_age - user_age

## Opción 1:
if age_difference < 0:
    if age_difference == -1:
        print("Sos más grande que yo solamente por un año.")
    else:
        print(f"Sos más grande que yo por {abs(age_difference)} años.")
elif age_difference > 0:
    if age_difference == 1:
        print("Soy más grande que vos solamente por un año.")
    else:
        print(f"Soy más grande que vos por {abs(age_difference)} años.")
else:
    print("Tenemos la misma edad.")

## Opción 2:
if age_difference == 0:
    print("Tenemos la misma edad.")
else:
    absolute_diff = abs(age_difference)
    tiempo = "año" if absolute_diff == 1 else "años"

    if age_difference > 0:
        print(f"Soy más grande que vos por {absolute_diff} {tiempo}.")
    else:
        print(f"Sos más grande que yo por {absolute_diff} {tiempo}.")

print()  ## Agrego un salto de línea.

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

#       Enter number one: 4
#       Enter number two: 3
#       4 is greater than 3

x = float(input("3. Ingresa un número x = "))
y = float(input("Ingresa un número y = "))

## Voy a utilizar una función, como para variar un poco.

print()  ## Agrego un salto de línea.

if x == y:
    print(f"x == y? -> {x == y}")
else:
    if max(x, y) == x:
        print(f"x > y? -> {x > y}")
    elif min(x, y) == x:
        print(f"y > x? -> {y > x}")

print()  ## Agrego un salto de línea.

print("Exercises: Level 2\n")

# 1. Write a code which gives grade to students according to theirs scores:

#       80-100, A
#       70-89, B
#       60-69, C
#       50-59, D
#       0-49, F


# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer


# 3. The following list contains some fruits:

#       fruits = ['banana', 'orange', 'mango', 'lemon']
#       If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')


print("Exercises: Level 3\n")

# 1. Here we have a person dictionary. Feel free to modify it!

#       person={
#           'first_name': 'Asabeneh',
#           'last_name': 'Yetayeh',
#           'age': 250,
#           'country': 'Finland',
#           'is_marred': True,
#           'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#           'address': {
#               'street': 'Space street',
#               'zipcode': '02210'
#           }
#           }

#        * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#        * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#        * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#        * If the person is married and if he lives in Finland, print the information in the following format:
#
#           Asabeneh Yetayeh lives in Finland. He is married.

print("🎉 CONGRATULATIONS ! 🎉\n")
