print("\n💻 Exercises: Day 8\n")

# 1. Create an empty dictionary called dog

dog = dict()

print(f"""1. Creé el diccionario llamado "dog": {dog}\n""")

# 2. Add name, color, breed, legs, age to the dog dictionary

dog["name"] = "Jackie Blue, mi amor."
dog["color"] = "Negro, blanco y con toques de marrón."
dog["breed"] = "Border Collie"
dog["legs"] = 4
dog["age"] = 2

print(f"""2. Añadí claves y valores al diccionario: {dog} \n""")

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    "first_name": "Juan Ignacio",
    "last_name": "Velazco Gez Schegtel",
    "gender": "M",
    "age": 25,
    "marital_status": "Soltero",
    "skills": ["Python", "C", "Linux"],
    "country": "Argentina",
    "city": "Goya",
    "address": "54 Studio, Driveway Ave.",
}

print(f"""3. Creé un diccionario "student": {student} \n""")

# 4. Get the length of the student dictionary

print(f"""4. La longitud del diccionario "student" es: {len(student)} \n""")

# 5. Get the value of skills and check the data type, it should be a list

habilidades = student.get("skills")

print(f"""5. Las habilidades (skills) son: {habilidades} \n""")

print(
    f"""El tipo de dato del valor hallado en la clave "skills" es: {type(habilidades)} \n"""
)

# 6. Modify the skills values by adding one or two skills

student["skills"].extend(["Pascal", "SQL", "SmallTalk", "Haskell"])

print(f"""6. Las habilidades (skills) han sido actualizadas: {student["skills"]} \n""")

# 7. Get the dictionary keys as a list

claves = dog.keys()

print(f"""7. Todas las claves del diccionario "dog" son: {claves} \n """)

# 8. Get the dictionary values as a list

valores = dog.values()

print(f"""8. Todos los valores del diccionario "dog" son: {valores} \n """)

# 9. Change the dictionary to a list of tuples using items() method

dog_lista_de_tuplas = dog.items()

print(
    f"""9. Ahora, tenemos el diccionario "dog" como una lista de tuplas: {dog_lista_de_tuplas}\n"""
)

# 10. Delete one of the items in the dictionary

student.pop("city")

print(f"""10. Eliminé la clave "city" del diccionario student: {student}\n""")

# 11. Delete one of the dictionaries

del student

try:
    print(f"""10. Diccionario "student": {student}""")
except Exception:
    print(
        """10. Si estás viendo este mensaje, es porque el diccionario "student" no existe más."""
    )

print("\n🎉 CONGRATULATIONS‼️  🎉")
