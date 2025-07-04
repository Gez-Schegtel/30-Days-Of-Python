from countries import COUNTRIES
from countries_data import COUNTRIES_DATA


def d10_level3() -> None:
    print("\nEstos son los ejercicios del día 10, nivel 3.\n")

    # ==============================
    #       Exercises: Level 3
    # ==============================

    # 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

    print("Punto 1:")

    countryland = [country for country in COUNTRIES if "land" in country]

    print(
        f"Todos los países que tienen 'land' son: {', '.join(map(str, countryland))}."
    )

    print()

    # 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

    print("Punto 2:")

    print("Versión 1: ")

    fruit_list = ["banana", "orange", "mango", "lemon"]
    list_lenght = len(fruit_list)

    for i in range(list_lenght - 1, -1, -1):
        print(f"{fruit_list[i]}, ", end=" ")

    print("\n\nVersión 2: ")

    for fruit in reversed(fruit_list):
        print(f"{fruit}, ", end=" ")

    print("\n\nVersión 3: ")

    for fruit in fruit_list[::-1]:
        print(f"{fruit}, ", end=" ")

    print("\n")

    # 3. Go to the data folder and use the countries_data.py file.
    #    1. What are the total number of languages in the data
    #    2. Find the ten most spoken languages from the data
    #    3. Find the 10 most populated countries in the world

    print("Punto 2:")

    total_lang = (
        set()
    )  # Al trabajar con un conjunto (set) me aseguro de no contar elementos repetidos.

    for dictionary in COUNTRIES_DATA:
        total_lang.update(dictionary.get("languages"))

    print(
        f"Los lenguajes que hay en la base de datos son: {', '.join(map(str, sorted(total_lang)))}."
    )
    print(f"\nRepresentan un total de {len(total_lang)} idiomas diferentes.\n")


if __name__ == "__main__":
    # Este condicional simple va acá para ejecutar este archivo de código fuente de forma específica si así se lo requiere.
    d10_level3()
