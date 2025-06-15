# ## 💻 Exercises: Day 5

# ### Exercises: Level 1

print("Ejercicios de nivel I:\n")

# 1. Declare an empty list
print(
    "1.Conozco dos formas de hacerlo: con los corchetes vacíos o con el método list()."
)

test_list = []

print(f"Lista vacía 1: {test_list}")

test_list = list()

print(f"Lista vacía 2: {test_list}\n")

# 2. Declare a list with more than 5 items
test_list = [number**2 for number in range(1, 5)]

print(
    f"""2. Creamos la siguiente lista y la almacenamos en la variable "test_list": {test_list}\n"""
)

# 3. Find the length of your list
print(f"3. Longitud de la lista: {len(test_list)}\n")

# 4. Get the first item, the middle item and the last item of the list
start_index = 0
last_index = len(test_list) - 1
middle_index = (start_index - last_index) // 2

print(f"4.Primer ítem: {test_list[start_index]}")
print(f"Último ítem: {test_list[last_index]}")
print(f"Ítem del medio: {test_list[middle_index]}\n")

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
test_list = [
    "Juan Ignacio",
    25,
    1.78,
    "Soltero",
    {
        "direccion_principal": "Saint Mary Boulevard 1518",
        "direccion_secundaria": "Malcom in the Middle Street",
    },
]

print(f"5. La lista que creé: {test_list}\n")

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Tutanota", "The Linux Foundation", "GNOME", "Canonical", "Debian"]

print("6. Lista creada.\n")

# 7. Print the list using print()
print(f"7. La lista es: {it_companies}.\n")

# 8. Print the number of companies in the list
print(f"8. La lista tiene {len(it_companies)} elementos.\n")

# 9. Print the first, middle and last company
start_index = 0
last_index = len(it_companies) - 1
middle_index = (start_index - last_index) // 2

print(f"9.Primer ítem: {it_companies[start_index]}")
print(f"Último ítem: {it_companies[last_index]}")
print(f"Ítem del medio: {it_companies[middle_index]}\n")

# 10. Print the list after modifying one of the companies
print("10. Ahora, cambiaré GNOME por KDE:\n")

it_companies[it_companies.index("GNOME")] = "KDE"

print(f"{it_companies}\n")

# 11. Add an IT company to it_companies
it_companies.append("Free Software Foundation")

print(f"11. Añadimos una nueva compañía al final: {it_companies}\n")

# 12. Insert an IT company in the middle of the companies list
## Voy a usar un método distinto para hallar el índice del medio.
middle_index = len(it_companies) // 2

it_companies.insert(middle_index, "OpenSUSE")

print(f"12. Insetamos una companía nueva en el medio de la lista: {it_companies}\n")

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
## Para este ejercicio voy a utilizar la comprensión de listas.
it_companies = [word.upper() if word == "Canonical" else word for word in it_companies]

print(f"13. Pasamos 'Canonical' a mayúsculas: {it_companies}\n")

# 14. Join the it_companies with a string '#; '
print(f"14. La lista pero ahora separadas por numerales: {' # '.join(it_companies)}\n")

## Recordar que el método join() devuelve una cadena, no una lista.
## print(type(" # ".join(it_companies))) -- Resultado: <class 'str'>

# 15. Check if a certain company exists in the it_companies list.
## EL siguiente método es sensible a minúsculas y mayúsculas.
if "Debian" in it_companies:
    print("15. Se encontró el elemento")
else:
    print("15. El elemento buscado no se encuentra.")

## Con el método presentado a continuación, no se tienen en cuenta las minúsculas y mayúsculas.
searched_item = "Debian"
search_result = any(searched_item.upper() == word.upper() for word in it_companies)

if search_result:
    print("15. Se encontró el elemento")
else:
    print("15. El elemento buscado no se encuentra.")

print("\n")

# 16. Sort the list using sort() method
print(f"16 Lista original: {it_companies}")
print(f"Lista ordenada de menor a mayor (alfabéticamente): {sorted(it_companies)}\n")

# 17. Reverse the list in descending order using reverse() method
print(
    f"17. Lista en ordenada en de mayor a menor (alfabéticamente): {sorted(it_companies, reverse=True)}\n"
)

# 18. Slice out the first 3 companies from the list
print(f"18. Quitamos los primeros tres elementos de la lista: {it_companies[3:]}\n")

# 19. Slice out the last 3 companies from the list
print(
    f"19. Quitamos los tres últimos elementos de la lista: {it_companies[: len(it_companies) - 3]}\n"
)

# 20. Slice out the middle IT company or companies from the list
list_length = len(it_companies)

print(f"Ahora, la lista tiene {list_length} elementos.\n")

if list_length % 2 == 0:
    print(
        f"20. Elementos del medio: {it_companies[(list_length // 2) - 1] + ' y ' + it_companies[list_length // 2]}"
    )
else:
    print(f"20. Elemento del medio: {it_companies[list_length // 2]}")

print("\n")

# 21. Remove the first IT company from the list
it_companies.pop(0)

print(f"21. Eliminé el primer elemento: {it_companies}\n")

# 22. Remove the middle IT company or companies from the list
list_length = len(it_companies)

print(f"Ahora, la lista tiene {list_length} elementos.\n")

middle_index = list_length // 2

if list_length % 2 == 0:
    it_companies.pop(middle_index)
    it_companies.pop(middle_index - 1)
else:
    it_companies.pop(middle_index)

print(
    f"22. Lista resultante luego de eliminar el/los elementos del medio: {it_companies}\n"
)

# 23. Remove the last IT company from the list
it_companies.pop()  # Por defecto, el método elimina el último elemento.

print(f"23. Eliminado el último elemento: {it_companies}\n")

# 24. Remove all IT companies from the list
it_companies.clear()

print(f"24. Eliminados todos los elementos: {it_companies}\n")

# 25. Destroy the IT companies list
del it_companies

try:
    print(f"25. Lista 'it_companies': {it_companies}")
except NameError:
    print("25. La lista 'it_companies' se borró por completo.")

print("\n")

# 26. Join the following lists:

#   front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#   back_end = ['Node','Express', 'MongoDB']

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

print(f"26. Listas unidas: {front_end + back_end}")

# Otro método:
## front_end.extend(back_end)
## print(f"Listas unidas: {front_end}\n")

# 27. After joining the lists in question 26, copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end + back_end

print(f"27. Full stack: {full_stack}")

full_stack_copy = full_stack.copy()
full_stack_copy.pop()  # borré el último elemento para comprobar el funcionamiento del método copy()

print(f"Full stack original: {full_stack}\nFull stack copy: {full_stack_copy}\n")

# ### Exercises: Level 2

print("Ahora empezamos con los ejercicios de nivel II.\n")

# 1. The following is a list of 10 students ages:

#   ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print(
    f"Para practicar antes de realizar los ejercicios, vemos dos métodos para ordenar listas.\n"
)

print(f"Antes del método sort(): {ages}\n")

ages.sort()

print(f"Utilizando el método sort(): {ages}\n")

ages = [
    19,
    22,
    19,
    24,
    20,
    25,
    26,
    24,
    25,
    24,
]  # Como el método sort() modifica la lista original, la tengo que volver a declarar para tener el orden original.

sorted(ages)

print(
    f"Utilizando el método sorted(): {ages} --> No se muestra ordenado porque este método no modifica la lista original.\n"
)

print(f"Utilizando el método sorted pero dentro de este print: {sorted(ages)}\n")

# - 1.1 Sort the list and find the min and max age

min_index = 0
max_index = len(ages) - 1

min_ages = sorted(ages)[min_index]
max_ages = sorted(ages)[max_index]

print(f"1.1 Edad más pequeña encontrada en la lista: {min_ages}")
print(f"1.1 Edad más grande encontrada en la lista: {max_ages}\n")

# - 1.2 Add the min age and the max age again to the list

ages.append(min_ages)
ages.append(max_ages)

print(f"1.2 La lista luego de agregar nuevamente la edad menor y mayor: {ages}\n")

# - 1.3 Find the median age (one middle item or two middle items divided by two)

if not ages:
    raise ValueError("La lista está vacía.")

list_length = len(ages)
middle_index = list_length // 2

ages.sort()  # ¡¡Es importante ordenar la lista para que los cálculos sean correctos!!

if list_length % 2 == 0:
    median = (ages[middle_index] + ages[middle_index - 1]) / 2
else:
    median = ages[middle_index]

print(f"1.3 La mediana de edad en la lista es de {median} años.\n")

# - 1.4 Find the average age (sum of all items divided by their number)

list_length = len(ages)
total_ages = 0

for _ in range(list_length):
    total_ages = total_ages + ages[_]

mean_age = total_ages / list_length
print(f"1.4.1 La media de edad es de {mean_age} años.")

total_ages = sum(
    ages
)  # Puedo "ahorrarme" la estructura manejada por contador utilizando el método sum().

print(
    f"1.4.2 La media de edad (con un método alternativo al clásico) es de {total_ages / list_length} años\n"
)

# - 1.5 Find the range of the ages (max minus min)

max_ages = max(
    ages
)  # Este método me permite obtener fácilmente la edad máxima, en comparación al punto 1.1.
min_ages = min(ages)  # Ídem a la línea de arriba, pero ahora con el mínimo.

ages_range = max_ages - min_ages

print(f"1.5 El rango de edad es de {ages_range} años.\n")

# - 1.6 Compare the value of (min - average) and (max - average), use abs() method

print(
    f"1.6 La edad más pequeña menos la media es: {min_ages} - {mean_age} = {abs(min_ages - mean_age)}"
)

print(
    f"1.6 La edad más grande menos la media es: {max_ages} - {mean_age} = {abs(max_ages - mean_age)}\n"
)

# 2. Find the middle country(ies) in the countries list

countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cape Verde",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombi",
    "Comoros",
    "Congo (Brazzaville)",
    "Congo",
    "Costa Rica",
    "Cote d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor Timur)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia, The",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macedonia",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia and Montenegro",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Swaziland",
    "Sweden",
    "Switzerland",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]

if not countries:
    raise ValueError("La lista de países está vacía.")

list_length = len(countries)
middle_index = list_length // 2

if list_length % 2 == 0:
    mid_countries = f"{countries[middle_index - 1]} y {countries[middle_index]}"
    print(
        f"2. Los países que se encuentran en la mitad de la lista son {mid_countries} en la posición {middle_index - 1} y {middle_index} respectivamente.\n"
    )
else:
    mid_country = countries[middle_index]
    print(
        f"2. El país que se encuentra en la mitad de la lista es {mid_country} en la posición {middle_index}.\n"
    )

# 3. Divide the countries list into two equal lists if it is even if not one more country for the first half.

list_length = len(countries)
middle_index = list_length // 2

if list_length % 2 == 0:
    print(f"3. La lista es par con {list_length} países.\n")
    first_half = countries[:middle_index]
    second_half = countries[middle_index:]
else:
    print(f"3. La lista es impar con {list_length} países.\n")
    first_half = countries[: middle_index + 1]
    second_half = countries[middle_index + 1 :]

print(f"Primera mitad con {len(first_half)} elementos: {first_half}\n")
print(f"Segunda mitad con {len(second_half)} elementos: {second_half}\n")

# 4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

another_countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]

first, second, third, *scandic_countries = another_countries

print(f"4. Primer país: {first}")
print(f"Segundo país: {second}")
print(f"Tercer país: {third}")
print(f"El resto, países escandinavos: {scandic_countries}\n")

# 🎉 CONGRATULATIONS ! 🎉

print("🎉 CONGRATULATIONS! 🎉\n")
