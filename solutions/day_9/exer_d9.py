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

score = int(input("1. Enter your score: "))

while score not in range(0, 101):
    score = int(
        input("Enter your scores again. It has to be a value between 0 and 100: ")
    )
print("\n")

if score in range(0, 50):
    print("Your grade is: F")
elif score in range(50, 60):
    print("Your grade is: D")
elif score in range(60, 70):
    print("Your grade is: C")
elif score in range(70, 90):
    print("Your grade is: B")
elif score in range(90, 101):
    print("Your grade is: A")

print("\n")

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
## Versión con listas.
autumn = ["september", "october", "november"]
winter = ["december", "january", "february"]
spring = ["march", "april", "may"]
summer = ["june", "july", "august"]

month_by_user = input("2. Enter the actual month of the year: ").lower().strip()
print("\n")

if month_by_user in autumn:
    print("The season is autumn!")
elif month_by_user in winter:
    print("The season is winter!")
elif month_by_user in spring:
    print("The season is spring!")
elif month_by_user in summer:
    print("The season is summer!")
else:
    print("Invalid input.")

print("\n")

## Versión con diccionario.
seasons = {
    **dict.fromkeys(["september", "october", "november"], "Autumn"),
    **dict.fromkeys(["december", "january", "february"], "Winter"),
    **dict.fromkeys(["march", "april", "may"], "Spring"),
    **dict.fromkeys(["june", "july", "august"], "Summer"),
}

season = seasons.get(month_by_user)

if season:
    print(f"The season is {season}!")
else:
    print("Invalid input.")

print("\n")

# 3. The following list contains some fruits:

#       fruits = ['banana', 'orange', 'mango', 'lemon']
#       If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ["banana", "orange", "mango", "lemon"]

fruit_by_user = input("3. Enter a fruit: ").lower().strip()
print("\n")

if fruit_by_user not in fruits:
    fruits.append(fruit_by_user)
    print(f"We added the fruit you suggested into our list: {fruits}")
else:
    print("That fruit already exist in the list.")

print("\n")

print("Exercises: Level 3\n")

# 1. Here we have a person dictionary. Feel free to modify it!

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# * If the person is married and if he lives in Finland, print the information in the following format:
#
# Asabeneh Yetayeh lives in Finland. He is married.


def middle_in_a_list(number_of_ex, listy):
    listy_len = len(listy)

    if listy_len % 2 != 0:
        middle_item = [listy[listy_len // 2]]
        print(
            f"{number_of_ex}. La habilidad que está en el medio de la lista es: {middle_item}"
        )
    else:
        middle_item = [listy[listy_len // 2 - 1], listy[listy_len // 2]]
        print(
            f"{number_of_ex}. Las habilidades que están en el medio de la lista son: {middle_item}"
        )


def python_skills_checker(number_of_ex, listy):
    listy = [word.upper() for word in listy]  ## List comprehension
    if "PYTHON" in listy:
        print(f"{number_of_ex}. La persona tiene habilidades en Python.")


def checking_developer_type(number_of_ex, listy):
    setsy = {word.upper() for word in listy}  ## Set comprehension

    if {"REACT", "NODE", "MONGODB"}.issubset(setsy):
        print(f"{number_of_ex}. He is a fullstack developer.")
    elif {"PYTHON", "NODE", "MONGODB"}.issubset(setsy):
        print(f"{number_of_ex}. He is a backend developer.")
    elif {"JAVASCRIPT", "REACT"}.issubset(setsy):
        print(f"{number_of_ex}. He is a frontend developer.")
    else:
        print(f"{number_of_ex}. Superunknown title.")


def checking_civil_state(number_of_ex, dicty):
    married = dicty.get("is_married")
    country = dicty.get("country")

    if married and country.upper() == "FINLAND":
        print(
            f"{number_of_ex}. {dicty.get('first_name')} {dicty.get('last_name')} is married and lives in Finland."
        )


skills = person.get("skills")

if skills:
    middle_in_a_list(1, skills)
    python_skills_checker(2, skills)
    checking_developer_type(3, skills)
else:
    print("""La clave "skills" buscada no se encuentra en la lista.""")


checking_civil_state(4, person)

print()

print("🎉 CONGRATULATIONS ! 🎉\n")
