# 💻 Exercises: Day 7

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

# 1. Join A and B


# 2. Find A intersection B


# 3. Is A subset of B


# 4. Are A and B disjoint sets


# 5. Join A with B and B with A


# 6. What is the symmetric difference between A and B


# 7. Delete the sets completely


# Exercises: Level 3

#     1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?


#     2. Explain the difference between the following data types: string, list, tuple and set


#     3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.


# 🎉 CONGRATULATIONS ! 🎉
