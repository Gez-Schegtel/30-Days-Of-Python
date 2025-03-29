# 💻 Exercises: Day 6

# Exercises: Level 1

print("Ejercicios de nivel 1: \n")

# 1. Create an empty tuple
## Primera forma:

first_tuple = ()

print(f"1. Tupla hecha con la primera forma {first_tuple}")

second_tuple = tuple()

print(f"Tupla hecha con la segunda forma {second_tuple}\n")

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers = ("Mauri", "Yamil", "Agus")
sisters = ("Coni", "Leonor")

print(f"2. Mis hermanos: {brothers}")
print(f"Mis hermanas: {sisters}\n")

# 3. Join brothers and sisters tuples and assign it to siblings

siblings = brothers + sisters

print(f"3. Mis hermanos son {siblings}\n")

# 4. How many siblings do you have?

siblings_count = len(siblings)

print(f"4. Tengo {siblings_count} hermanos en total.\n")

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

## Convertimos la tupla en una lista para poder modificarla.

family_members = list(siblings)

my_parents = ["Alfredo", "Marisa"]

family_members.extend(my_parents)

family_members = [
    real_family
    for real_family in family_members
    if real_family in my_parents or real_family == "Coni"
]

print(f"5. Mi familia es {family_members}\n")

# Exercises: Level 2

print("Ejercicios de nivel 2: \n")

# 1. Unpack siblings and parents from family_members

sibling, *parents = family_members[0], family_members[1:]

print(f"1. Mi hermana es {sibling}")
print(f"Mis padres son {parents}\n")

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ("Naranja", "Ananá", "Frutilla", "Pomelo")

vegetables = ("Rúcula", "Zapallo", "Tabaco")

animal_products = ("Royal Canin", "Infinity", "Michi Feliz")

food_stuff_tp = fruits + vegetables + animal_products

print(f"2. La variable food_stuff_tp contiene: {food_stuff_tp}\n")

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)

print(f"3. La variable food_staff_lt contiene: {food_stuff_lt}\n")

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

tuple_len = len(food_stuff_tp)
mid_index = tuple_len // 2

if tuple_len % 2 == 1:
    print(
        f"4. El elemento del medio de la variable food_stuff_tp es: {food_stuff_tp[mid_index]}"
    )
else:
    print(
        f"4. Los elementos del medio de la variable food_stuff_tp son: {food_stuff_tp[mid_index - 1]} y {food_stuff_tp[mid_index]}"
    )

print("\n")

# 5. Slice out the first three items and the last three items from food_staff_lt list

first_index = 0
last_index = len(food_stuff_tp) - 1

print(
    f"5. Removiendo los primeros y últimos tres elementos de la variable food_stuff_tp nos queda la siguiente tupla: {food_stuff_tp[first_index + 3 : last_index - 2]}\n"
)

# 6. Delete the food_staff_tp tuple completely

del food_stuff_tp

try:
    print(
        f"6. Probamos si podemos mostrar por pantalla la tupla eliminada: {food_stuff_tp}"
    )
except NameError:
    print("6. La tupla fue eliminada exitosamente.")

print("\n")

# 7. Check if an item exists in tuple:

#       Check if 'Estonia' is a nordic country

#       Check if 'Iceland' is a nordic country

#       nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

if "Estonia" in nordic_countries:
    print("7. Estonia es un país nórdico.")
else:
    print("7. Estonia no es un país nórdico.")

if "Iceland" in nordic_countries:
    print("Iceland es un país nórdico.")
else:
    print("Iceland no es un país nórdico.")

print("\n¡Felicitaciones!\n")
