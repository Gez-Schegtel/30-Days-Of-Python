# Ejercicio 1: Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
strings = ['Thirty', 'Days', 'of', 'Python']
print(f"1. {' '.join(strings)}\n")

# Ejercicio 2: Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Club Atlético River Plate'.
print(f"2. {' '.join(['Coding', 'For', 'All'])}\n")

# Ejercicio 3: Declare a variable named my_club and assign it to an initial value "Club Atlético River Plate".
my_club = "Club Atlético River Plate"

# Ejercicio 4: Print the variable my_club using print().
print(f"4. {my_club}\n")

# Ejercicio 5: Print the length of the my_club string using len() method and print().
print(f"5. {len(my_club)}\n")

# Ejercicio 6: Change all the characters to uppercase letters using upper() method.
print(f"6. {my_club.upper()}\n")

# Ejercicio 7: Change all the characters to lowercase letters using lower() method.
print(f"7. {my_club.lower()}\n")

# Ejercicio 8: Use capitalize(), title(), swapcase() methods to format the value of the string Club Atlético River Plate.
print(f"8.1 {my_club.capitalize()}\n")
print(f"8.2 {my_club.title()}\n")
print(f"8.3 {my_club.swapcase()}\n")

# Ejercicio 9: Cut(slice) out the first word of Club Atlético River Plate string.
string_split = my_club.split()
string_sliced = string_split[1:]
string_again = ' '.join(string_sliced)
print(f"9. Primero, usamos el método split para obtener una lista con todas las palabras de la cadena: {string_split}")
print(f"Ahora, obtenemos todas las palabras menos la primera (o sea, descartamos el primer elemento de la lista que creamos anteriormente): {string_sliced}")
print(f"Finalmente podemos convertir en un string la palabra recortada: {string_again}\n")

# Ejercicio 10: Check if Club Atlético River Plate string contains a word "Atlético" using the method index, find or other methods.
print("10. Este punto se puede resolver tanto con el método find() como con el método index().")
print("Si lo buscado no es encontrado por find(), este retorna el valor -1, a diferencia del método index() que devuelve una excpeción de error.")
print("Por lo demás, la sintaxis es idéntica. Yo lo voy a resolver con el método find():")

if my_club.find('Atlético') != -1:
    print("La palabra se encontró.")
else:
    print("La palabra buscada no se encontró.")

print("\n")

# Ejercicio 11: Replace the word Atlético in the string 'Club Atlético River Plate' to Genial.
print(f"11. {my_club.replace('Atlético', 'Genial')}\n")

# Ejercicio 12: Change Python for Everyone to Python for All using the replace method or other methods.
test_text = "Python for Everyone"
print(f"12. {test_text.replace('Everyone', 'All')}\n")

# Ejercicio 13: Split the string 'Club Atlético River Plate' using space as the separator (split()).
print(f"13. {my_club.split(' ')}\n")

# Ejercicio 14: "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
test_text = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon, The Linux Foundation, Debian"
print(f"14. {test_text.split(',')}\n")

# Ejercicio 15: What is the character at index 0 in the string Club Atlético River Plate.
print(f"15. {my_club[0]}\n")

# Ejercicio 16: What is the last index of the string Club Atlético River Plate.
print(f"16. {my_club[-1]}\n")

# Ejercicio 17: What character is at index 10 in "Club Atlético River Plate" string.
print(f"17. {my_club[10]}\n")

# Ejercicio 18: Create an acronym or an abbreviation for the name 'Python For Everyone'.
test_text = 'Python for Everyone'

## La siguiente es mi versión:
test_list = test_text.split()
word_number = len(test_list)
acronym = ""

for n in range(0, word_number):
    acronym = acronym + test_list[n][0].upper()

print(f"18.1 {acronym}")

## Versión del ChatGPT 4-o:
acronym = ''.join([word[0].upper() for word in test_text.split()])
print(f"18.2 {acronym}\n")

# Ejercicio 19: Create an acronym or an abbreviation for the name 'Club Atlético River Plate'.
test_list = my_club.split()
print(f"19. La lista con la que formaremos el acrónimo es: {test_list}")

acronym = ''.join(word[0].upper() for word in test_list)
print(f"El acrónimo es: {acronym}\n")

# Ejercicio 20: Use index to determine the position of the first occurrence of C in Club Atlético River Plate.
search_result = my_club.find('C')

if search_result != -1:
    print(f"20. La primer letra 'C' en la palabra {my_club} se encontró en la posición: {search_result + 1}")
else:
    print("20. El caracter buscado no se encontró en la cadena de texto.")

print("\n")

# Ejercicio 21: Use index to determine the position of the first occurrence of F in Club Atlético River Plate.
try:
    search_result = my_club.index('F')
    print(f"21. La primer letra 'F' en la palabra {my_club} se encontró en la posición: {search_result + 1}")
except ValueError:
    print("21. El caracter buscado no se encontró en la cadena de texto.")

print("\n")

# Ejercicio 22: Use rfind to determine the position of the last occurrence of l in Club Atlético River Plate People.
## No recorre la cadena en reversa, pero sí retorna la posición de la última coincidencia. Equivale a buscar todas las ocurrencias y quedarse con la de mayor índice.
search_result = my_club.rfind('l')

if search_result != -1:
    print(f"22. La última letra 'l' en la palabra {my_club} se encontró en la posición: {search_result + 1}")
else:
    print("22. El caracter buscado no se encontró en la cadena de texto.")

print("\n")

# Ejercicio 23: Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'.
test_text = 'You cannot end a sentence with because because because is a conjunction'
search_result = test_text.find('because')

if search_result != -1:
    print(f'''23. La primera ocurrencia de 'because' en "{test_text}" se dio en el caracter: {search_result + 1}''')
    try:
        search_result = test_text.split(' ').index('because')
        print(f"La primer ocurrencia se dio en la palabra número: {search_result + 1}")
    except ValueError:
        print("La palabra solicitada no se encuentra en el texto.")
else:
    print("23. No se encontró la palabra solicitada.")

print("\n")

# Ejercicio 24: Use rindex to find the position of the last occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'.
test_text = 'You cannot end a sentence with because because because is a conjunction'
test_list = test_text.split(' ')
search_result = test_text.rindex('because')

if search_result != -1:
    print(f'''24. La última ocurrencia de 'because' en "{test_text}" se dio en el caracter: {search_result + 1}''')
    try:
        search_result = len(test_list) - 1 - test_list[::-1].index('because')
        print(f"La última ocurrencia se dio en la palabra número: {search_result + 1}")
    except ValueError:
        print("La palabra solicitada no se encuentra en el texto.")
else:
    print("24. No se encontró la palabra solicitada.")

print("\n")

# Ejercicio 25: Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'.
## No entendí se se refiere a esto...
phrase_to_slice = 'because because because '
print(f"25.1 {test_text.replace(phrase_to_slice, '')}")

## ... o a esto:
start_index = test_text.find(phrase_to_slice) # Índice donde empieza la frase.

if start_index != -1:
    sliced_phrase = test_text[start_index : start_index + len(phrase_to_slice)]
    print(f"25.2 {sliced_phrase}")
else:
    print("25.2 La frase no se encontró en la oración.")

print("\n")

# Ejercicio 26: Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'.
test_list = test_text.split()
test_list_upper = [ word.upper() for word in test_list ] # Para modificar lo que ya había hecho antes, ahora utilizando la comprensión de listas paso a mayúsculas todas las palabras para asegurarme de enonctrar la palabra sin importar el "casing".

try:
    search_result = test_list_upper.index('BECAUSE') + 1
    print(f"26. {search_result}")
except ValueError:
    print("26. No se encontró la palabra.")

print("\n")

# Ejercicio 27: Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'.
start_index = test_text.find('because')

print(f"27. {test_text[start_index:start_index + len(phrase_to_slice)]}\n")

# Ejercicio 28: Does 'Club Atlético River Plate' start with a substring Club?
print(f'''28. ¿El texto "{my_club}" comienza con "Club"?: {my_club.startswith('Club')}\n''')

# Ejercicio 29: Does 'Club Atlético River Plate' end with a substring club?
print(f'''29. ¿El texto "{my_club}" termina con "club"?: {my_club.endswith('Club')}\n''')

# Ejercicio 30: '   Club Atlético River Plate      '  , remove the left and right trailing spaces in the given string.
test_text = '   Club Atlético River Plate      '
print(f'''30. Sacamos los espacios innecesarios: "{test_text.strip()}"\n''')

# Ejercicio 31: Which one of the following variables return True when we use the method isidentifier():
#     30DaysOfPython
#     thirty_days_of_python
print(f'''31.1 Is "30DaysOfPython" and identifier?: {'30DaysOfPython'.isidentifier()}''')
print(f'''31.2 Is "thirty_days_of_python" and identifier?: {'thirty_days_of_python'.isidentifier()}\n''')

# Ejercicio 32: The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Join the list with a hash with space string.
test_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print(f"32. {' # '.join(test_list)}\n")

# Ejercicio 33: Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print("33. I am enjoying this challenge.\n\n ... I just wonder what's next.\n")

# Ejercicio 34: Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("34.\nName\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki\n")

# Ejercicio 35: Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
## Voy a usar f-strings porque son más eficientes y me gustan más.
radius = 10
area = 3.14 * radius ** 2

print(f"35. The area of a circle with radius {radius} is {area} meters square.\n")

# Ejercicio 36: Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
## Ídem a 35.
a, b = 8, 6
print(f"36. {a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")

