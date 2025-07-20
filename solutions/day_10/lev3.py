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

    # Aclaración: No era necesario el uso de una estructura iterativa para conseguir lo que se pide en esta consigna. Considero que lo más eficiente sería utilizar la técnica de "List Slicing". Con escribir `fruit_list[::-1]` (sin usar ningún loop) se consigue el mismo efecto.

    print("\n")

    # 3. Go to the data folder and use the countries_data.py file.
    #    1. What are the total number of languages in the data
    #    2. Find the ten most spoken languages from the data
    #    3. Find the 10 most populated countries in the world

    print("Punto 3.")
    print("Parte 3.1: ")

    # Al trabajar con un conjunto (set) me aseguro de no contar elementos repetidos:
    total_lang = set()

    for country in COUNTRIES_DATA:
        # Se declara que en caso de no encontrar un "language" se devuelva una lista vacía para evitar errores.
        total_lang.update(country.get("languages", list()))

    print(
        f"Los lenguajes que hay en la base de datos son: {', '.join(map(str, sorted(total_lang)))}."
    )
    print(f"\nRepresentan un total de {len(total_lang)} idiomas diferentes.\n")

    print("Parte 3.2: ")

    languages_info = dict()

    for country in COUNTRIES_DATA:
        for language in country["languages"]:
            if language not in languages_info:
                languages_info[language] = {
                    "countries": {country["name"]},
                    "count": 1,
                    "population": country["population"],
                }
            else:
                languages_info[language]["countries"].add(country["name"])
                languages_info[language]["count"] += 1
                languages_info[language]["population"] += country["population"]

    languages_top_by_country = sorted(
        languages_info.items(), key=lambda item: item[1]["count"], reverse=True
    )[:10]

    languages_top_by_population = sorted(
        languages_info.items(), key=lambda item: item[1]["population"], reverse=True
    )[:10]

    for i, (lang, data) in enumerate(languages_top_by_country, 1):
        print(f"{i}. {lang:<25} -- {data['count']:>2} países")

    print("\n")

    for i, (lang, data) in enumerate(languages_top_by_population, 1):
        print(f"{i}. {lang:<25} -- {data['population']:,} personas")

    print("\nParte 3.3: ")

    population_top_by_country = sorted(
        COUNTRIES_DATA, key=lambda item: item["population"], reverse=True
    )[:10]

    # # Ejemplo de emisión por pantalla con la técnica "tradicional"
    # for i in range(len(population_top_by_country)):
    #     print(
    #         f"{i + 1}. {population_top_by_country[i]['name']:<25} -- {population_top_by_country[i]['population']:,} habitantes"
    #     )

    for i, country in enumerate(population_top_by_country, 1):
        print(f"{i}. {country['name']:<25} -- {country['population']:,} habitantes")


if __name__ == "__main__":
    # Este condicional simple va acá para ejecutar este archivo de código fuente de forma específica si así se lo requiere.
    d10_level3()
