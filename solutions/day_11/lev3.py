# ~~~~~~~~ Aclaración ~~~~~~~~ #
# Estaba cansado, así que hice estos ejercicios con la IA Grok. Analicé y estructuré el archivo de código fuente, nada más.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

from countries_data import COUNTRIES_DATA


def d11_level3():
    # 1. Function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    print(
        f"{is_prime(int(input('Ingresá un número para analizar si es primo o no: ')))}\n"
    )

    # 2. Function to check if all items are unique in the list
    def all_unique(lst):
        return len(lst) == len(set(lst))

    print(
        f"{all_unique(list(input('Ingresá una lista y veamos si todos los elementos que ingresás son iguales: ').split()))}\n"
    )

    # 3. Function to check if all items of the list are of the same data type
    def same_type(lst):
        if not lst:
            return True
        first_type = type(lst[0])
        return all(type(item) is first_type for item in lst)

    test_list = ["River", "Plate", 9, 12, 18]
    print(
        f"¿Los elementos de la lista {test_list} son todos del mismo tipo? -> {same_type(test_list)}\n"
    )

    test_list = ["River", "Plate", "9", "12", "18"]
    print(
        f"¿Los elementos de la lista {test_list} son todos del mismo tipo? -> {same_type(test_list)}\n"
    )

    # 4. Function to check if provided variable is a valid Python variable name
    import keyword

    def is_valid_variable(name):
        if not isinstance(name, str):
            return False
        if keyword.iskeyword(name):
            return False
        return name.isidentifier()

    variable_bien = "good_var"
    print(
        f"¿El nombre de variable < {variable_bien} > es válido? -> {is_valid_variable(variable_bien)}"
    )

    variable_wtf = 4
    print(
        f"¿El nombre de variable < {variable_wtf} > es válido? -> {is_valid_variable(variable_wtf)}\n"
    )

    # 5.a) Function to get the most spoken languages by total population where they are official
    from collections import defaultdict

    def most_spoken_languages(countries_data, num=10):
        lang_pop = defaultdict(int)
        for country in countries_data:
            population = country["population"]
            for lang in country["languages"]:
                lang_pop[lang] += population
        sorted_langs = sorted(lang_pop.items(), key=lambda x: x[1], reverse=True)
        return sorted_langs[:num]

    print(f"Los lenguajes más hablados son: {most_spoken_languages(COUNTRIES_DATA)}\n")

    # 5.b) Function to get the most populated countries
    def most_populated_countries(countries_data, num=10):
        sorted_countries = sorted(
            countries_data, key=lambda x: x["population"], reverse=True
        )
        return [
            (country["name"], country["population"])
            for country in sorted_countries[:num]
        ]

    print(
        f"Los países con más habitantes son: {most_populated_countries(COUNTRIES_DATA)}"
    )


if __name__ == "__main__":
    d11_level3()
