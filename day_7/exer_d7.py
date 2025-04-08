# 💻 Exercises: Day 7

print("💻 Ejercicios: nivel 1\n")

it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Definimos los siguientes conjuntos (sets): \n")
print("it_companies: ", it_companies)
print("A: ", A)
print("B: ", B)
print("age: ", age)

# Exercises: Level 1

# 1. Find the length of the set it_companies

print(f"\n1. La longitud del conjunto 'it_companies' es: {len(it_companies)}\n")

# 2. Add 'Twitter' to it_companies

it_companies.add("Twitter")
print(f"2. Agregamos la empresa 'Twitter' al conjunto 'it_companies': {it_companies}\n")

# 3. Insert multiple IT companies at once to the set it_companies

more_it_companies = {"Debian", "Canonical", "MariaDB", "The Linux Foundation"}

print(
    f"3. Las empresas que quiero agregar al conjunto 'it_companies' son las siguientes: {more_it_companies}\n"
)

print(
    f"Con el método 'union()' podemos hacer esto sin modificar el conjunto orignal: {it_companies.union(more_it_companies)}\n"
)

it_companies.update(more_it_companies)

print(f"Con el método 'update()' modifico el conjunto original: {it_companies}\n")

# 4. Remove one of the companies from the set it_companies

print(
    "4. Para eliminar elementos, se puede utilizar los métodos 'pop()', 'remove()' y 'discard()'.\n"
)

# it_companies.clear()  # Esto lo hago para probar el error que levanta el método pop().

try:
    elemento_eliminado = it_companies.pop()  # Hacemos esto de guardar el elemento eliminado porque por defecto pop() borra algo pero no sabemos qué.

    print(
        f"El elemento que se eliminó de la lista con 'pop()' fue {elemento_eliminado}.\nLa lista quedó así: {it_companies}\n"
    )
except KeyError:
    print("No se puede utilizar el método 'pop()' porque la lista está vacía.\n")


a_eliminar = "Apple"

try:
    it_companies.remove(a_eliminar)
    print(
        f"Con el método 'remove()' eliminamos el elemento {a_eliminar}: {it_companies}\n"
    )
except KeyError as no_encontrado:
    print(
        f"No es posible borrar el elemento {no_encontrado} porque el mismo no se encuentra en el conjunto. Seguramente el método 'pop()' ejecutado anteriormente lo haya borrado.\n"
    )

a_eliminar = "Facebook"
it_companies.discard(
    a_eliminar
)  # Este método no devuelve ningún error, por lo que no es necesario el bloque "try: pass except Exception as e: raise "

print(
    f"Con el método 'discard()' eliminamos (si es que no se lo borró anteriormente) al elemento {a_eliminar}: {it_companies}\n"
)

# 5. What is the difference between remove, pop and discard

print(
    "5. El método 'pop()' elimina un elemento cualquiera del conjunto. Devuelve el elemento eliminado, por lo que te da la opción de guardar o mostrar por pantalla cuál fue el elemento que se borró. En caso de estar vacío el conjunto, levanta un error del tipo KeyError. No acepta parámetros.\n"
)

print(
    "El método 'remove()' toma como parámetro el elemento que quieras eliminar del conjunto. En caso de no encontrarse el elemento, el método devuelve el error KeyError. El método no devuelve nada en caso de haber hecho la eliminación.\n"
)

print(
    "El método 'discard()' funciona igual que el método 'remove()', pero no arroja ningún código de error en caso de no poder efectuar la eliminación del elemento. En estos casos no hace nada.\n"
)

# Exercises: Level 2

print("💻 Ejercicios: nivel 2\n")

print("Utilizaremos los siguientes conjuntos...\n")
print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}\n")

# 1. Join A and B

print(
    "1. Para hacer una unión entre dos conjuntos se puede utilizar el método 'union()' o el operador '|':\n"
)

print(f"A.union(B) >> {A.union(B)}")
print(f"A | B >> {A | B}\n")

# 2. Find A intersection B

print(
    "2. Para la intersección se puede utilizar el método 'intersec()' o el operador '&'.\n"
)

print(f"A.intersection(B) >> {A.intersection(B)}")
print(f"A & B >> {A & B}\n")

# 3. Is A subset of B

print(
    "3. Podemos usar el operador '<=' o el método 'issubset()' para ver si un conjunto es un subconjunto de otro.\n"
)

print(f"¿Es A un subconjunto de B? A.issubset(B) >> {A.issubset(B)}")
print(f"¿Es A un subconjunto de B? A <= B >> {A <= B}\n")

# 4. Are A and B disjoint sets

print(
    "4. Para ver si dos conjuntos son disjuntos (o sea, si no tienen ningún elemento en común) no nos queda más que utilizar el método 'isdisjoint()'\n"
)

print(f"¿Son A y B conjuntos disjuntos? >> {A.isdisjoint(B)}\n")

# 5. Join A with B and B with A

print("5. La unión es conmutativa, por lo que da igual si unís A con B, o B con A.\n")

print(f"A.union(B) >> {A.union(B)}")
print(f"B.union(A) >> {B.union(A)}\n")

# 6. What is the symmetric difference between A and B

print(
    "6. Recordar que la diferencia simétrica de dos conjuntos es el conjunto que contiene todos los elementos que no tienen en común dichos conjuntos.\nEn Python lo podemos encontrar con el método 'symmetric_difference()' o el operador '^'.\n"
)

print(f"A.symmetric_difference(B) >> {A.symmetric_difference(B)}")
print(f"A ^ B >> {A ^ B}\n")

# 7. Delete the sets completely

print(
    "7. Podemos usar 'clear()' para eliminar todos los elementos de un conjunto. Para borrarlo definitivamente hay que usar el método 'del'."
)

A.clear()

print(f"El conjunto A después de haber hecho 'A.clear()' >> {A}")

del B

try:
    print(f"El conjunto B luego de haber hecho 'del B' >> {B}")
except Exception:
    print(
        "No se puede mostrar el conjunto B, pues luego de haber hecho 'del B' éste ya no existe más."
    )

print("\n")

# Exercises: Level 3

print("💻 Ejercicios: nivel 3\n")

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age_set = set(age)

print(
    f"1. ¿El conjunto de edades {age_set} tiene una cardinalidad mayor a la lista de edades {age}?\n"
)
print(f"Cardinalidad del conjunto: {len(age_set)}")
print(f"Cardinalidad de la lista: {len(age)}\n")

print(
    "Esto es así porque los conjuntos no admiten elementos repetidos, situación que sí se puede dar en las listas.\n"
)

# 2. Explain the difference between the following data types: string, list, tuple and set

print(
    "2. ¡Atención! Al siguiente punto lo hice con DeepSeek porque no tenía muchas ganas de escribir.\n"
)

explicacion = """
Diferencias entre String, List, Tuple y Set en Python:

1. 🔤 String:
   - Inmutable (no se puede modificar después de crear)
   - Secuencia de caracteres
   - Sintaxis: "hola" o 'mundo'
   - Ejemplo: 'Python' → 'P','y','t','h','o','n'. Aclaración: Esta notación pretende demostrar que cada letra de la cadena tiene un índice. La 'P' tiene un índice de 0, y así sucesivamente con las demás letras.

2. 📃 List:
   - Mutable (se puede modificar)
   - Ordenada y indexada
   - Permite elementos duplicados
   - Sintaxis: [1, 2, 3]
   - Ejemplo: [10, "texto", True] → Puede tener distintos tipos

3. 📦 Tuple:
   - Inmutable (como una lista fija)
   - Más rápida que las listas
   - Sintaxis: (1, 2, 3)
   - Ejemplo: (255, 0, 128) → Usado para datos constantes

4. 🎯 Set:
   - Mutable pero con elementos únicos (no duplicados)
   - No ordenado ni indexado
   - Sintaxis: {1, 2, 3}
   - Ejemplo: {1, 2, 2, 3} → Se convierte en {1, 2, 3}

🔑 Key Differences:
   ┌──────────┬──────────┬──────────┬──────────┬──────────┐
   │          │ Mutable  │ Ordenado │ Indexado │ Únicos   │
   ├──────────┼──────────┼──────────┼──────────┼──────────┤
   │ String   │    ❌    │    ✅    │    ✅    │    ❌    │
   │ List     │    ✅    │    ✅    │    ✅    │    ❌    │
   │ Tuple    │    ❌    │    ✅    │    ✅    │    ❌    │
   │ Set      │    ✅    │    ❌    │    ❌    │    ✅    │
   └──────────┴──────────┴──────────┴──────────┴──────────┘
"""

print(explicacion)

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

print(
    "3. Voy a sacar los puntos '.' de la oración para pracicar la comprensión de listas.\n"
)

oracion_str = "I am a teacher and I love to inspire and teach people."

print(f"oracion_str: {oracion_str}\nTipo: {type(oracion_str)}\n")

oracion_list = list(oracion_str)

print(f"oracion_list: {oracion_list}\nTipo: {type(oracion_list)}\n")

oracion_list_filtrada = [char for char in oracion_list if char != "."]

print(
    f"oracion_list_filtrada: {oracion_list_filtrada}\nTipo: {type(oracion_list_filtrada)}\n"
)

oracion_str_filtrada = "".join(oracion_list_filtrada)

print(
    f"oracion_str_filtrada reconstruida: {oracion_str_filtrada}\nTipo: {type(oracion_str_filtrada)}\n"
)

unique_words = set(oracion_str_filtrada.split())

print(
    f'''3. El número de palabras únicas utilizadas en la oración "{oracion_str_filtrada}" es de {len(unique_words)}.\n'''
)


print("🎉 CONGRATULATIONS ! 🎉\n")
