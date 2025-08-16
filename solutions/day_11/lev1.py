def d11_level1():
    print("\n### Ejercicios: Día 11, nivel 1. ###\n")

    # 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.

    def add_two_numbers(n1, n2):
        return n1 + n2

    print(f"Utilizando una función tradicional: {add_two_numbers(6, 4)}")

    # A continuación voy a probar cómo utilizar una función lambda, aunque la siguiente forma de utilizarla no es considerada una práctica muy buena que digamos.
    add_two_numbers_lambda = lambda n1, n2: n1 + n2

    print(f"Utilizando una función lambda: {add_two_numbers_lambda(6, 4)}\n")

    # 2. Area of a circle is calculated as follows: area = π × r × r. Write a function that calculates _area_of_circle_.

    # A continuación voy a probar cómo utilizar una función lambda, aunque la siguiente forma de utilizarla no es considerada una práctica muy buena que digamos.
    area_of_circle = lambda radius, pi=3.14: pi * radius**2

    print(f"Radio de un círculo de radio 4: {area_of_circle(4)}\n")

    # 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

    def add_all_nums(*numbers):
        sum = 0
        for number in numbers:
            if isinstance(number, (int, float)):
                sum += number
            else:
                print(
                    f"Advertencia: El valor '{number}' no es un número válido y se omitirá."
                )

        return sum

    print(f"Suma de varios números: {add_all_nums(1, 2, 3, 4, 'cuatro')}\n")

    # 4. Temperature in °C can be converted to °F using this formula: °F = (°C × 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.

    def convert_celsius_to_fahrenheit(cels_temp):
        fahr_temp = cels_temp * 9 / 5 + 32
        return fahr_temp

    print(
        f"32 grados celsius son {convert_celsius_to_fahrenheit(32)} grados fahrenheit.\n"
    )

    # 5. Write a function called check_season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

    def check_season(month: str, day: int) -> str:
        # Convierte el mes a minúsculas para manejar mayúsculas y minúsculas.
        month = month.lower()

        # Mapeo de nombres de meses a números para la lógica de la fecha.
        month_map = {
            "enero": 1,
            "febrero": 2,
            "marzo": 3,
            "abril": 4,
            "mayo": 5,
            "junio": 6,
            "julio": 7,
            "agosto": 8,
            "septiembre": 9,
            "octubre": 10,
            "noviembre": 11,
            "diciembre": 12,
        }

        # Validar el mes y el día.
        if month not in month_map or not (1 <= day <= 31):
            return "Por favor, ingresa un mes válido (nombre) y un día válido."

        month_num = month_map[month]

        # Verano: 21 de diciembre - 20 de marzo
        if (
            (month_num == 12 and day >= 21)
            or (month_num in [1, 2])
            or (month_num == 3 and day <= 20)
        ):
            return "¡Estamos en verano! ☀️"

        # Otoño: 21 de marzo - 20 de junio
        elif (
            (month_num == 3 and day >= 21)
            or (month_num in [4, 5])
            or (month_num == 6 and day <= 20)
        ):
            return "¡Estamos en otoño! 🍂"

        # Invierno: 21 de junio - 20 de septiembre
        elif (
            (month_num == 6 and day >= 21)
            or (month_num in [7, 8])
            or (month_num == 9 and day <= 20)
        ):
            return "¡Estamos en invierno! ☃️"

        # Primavera: 21 de septiembre - 20 de diciembre
        elif (
            (month_num == 9 and day >= 21)
            or (month_num in [10, 11])
            or (month_num == 12 and day <= 20)
        ):
            return "¡Estamos en primavera! 🌸"

        return "Fecha fuera de rango."

    month_today = "agosto"
    day_today = 14
    print(
        f"La fecha es {day_today} de {month_today}, por lo tanto... {check_season(month_today, day_today)}\n"
    )

    # 6. Write a function called calculate_slope which return the slope of a linear equation

    def calculate_slope(p1, p2):
        slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
        return slope

    point1 = (2, 5)
    point2 = (4, 8)

    print(
        f"La pendiente entre los puntos {point1} y {point2} es: {calculate_slope(p1=point1, p2=point2)}\n"
    )

    # 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
    import cmath

    def solve_quadratic(a: float, b: float, c: float) -> str:
        """
        Resuelve una ecuación cuadrática de la forma ax^2 + bx + c = 0.

        Args:
            a (float): El coeficiente del término cuadrático (x^2).
            b (float): El coeficiente del término lineal (x).
            c (float): El término constante.

        Returns:
            str: Una cadena de texto con las soluciones de la ecuación.
        """

        # Verificamos si el coeficiente 'a' es cero. Si lo es, no es una ecuación cuadrática.
        if a == 0:
            return "El coeficiente 'a' no puede ser cero para una ecuación cuadrática."

        # Calculamos el discriminante (delta)
        discriminant = (b**2) - 4 * a * c

        # Evaluamos el discriminante para determinar el tipo de soluciones
        if discriminant > 0:
            # Dos soluciones reales y distintas
            x1 = (-b - discriminant**0.5) / (2 * a)
            x2 = (-b + discriminant**0.5) / (2 * a)
            return f"La ecuación tiene dos soluciones reales: x1 = {x1} y x2 = {x2}"

        elif discriminant == 0:
            # Una única solución real
            x = -b / (2 * a)
            return f"La ecuación tiene una única solución real: x = {x}"

        else:
            # Dos soluciones complejas (usamos cmath para números complejos)
            x1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
            x2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
            return f"La ecuación tiene dos soluciones complejas: x1 = {x1} y x2 = {x2}"

    # --- Ejemplos de uso ---

    # Ejemplo 1: Dos soluciones reales (x^2 + 5x + 6 = 0)
    print("Ecuación: x^2 + 5x + 6 = 0")
    print(solve_quadratic(a=1, b=5, c=6))  # Debería mostrar: x1 = -3.0 y x2 = -2.0
    print("-" * 30)

    # Ejemplo 2: Una única solución real (x^2 - 4x + 4 = 0)
    print("Ecuación: x^2 - 4x + 4 = 0")
    print(solve_quadratic(a=1, b=-4, c=4))  # Debería mostrar: x = 2.0
    print("-" * 30)

    # Ejemplo 3: Dos soluciones complejas (x^2 + x + 1 = 0)
    print("Ecuación: x^2 + x + 1 = 0")
    print(solve_quadratic(a=1, b=1, c=1))  # Debería mostrar soluciones complejas
    print("-" * 30)

    # Ejemplo 4: Coeficiente 'a' igual a 0
    print("Ecuación: 0x^2 + 2x + 4 = 0")
    print(solve_quadratic(a=0, b=2, c=4))

    print()

    # 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

    def print_each_list_element(the_list):
        print("Los elementos de la lista son: ")
        for element in the_list:
            print(element)

    my_list = ["Milton Casco", "Paulo Díaz", "Franco Armani"]
    print_each_list_element(my_list)

    print()

    # 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

    # ```py
    # print(reverse_list([1, 2, 3, 4, 5]))
    # # [5, 4, 3, 2, 1]
    # print(reverse_list1(["A", "B", "C"]))
    # # ["C", "B", "A"]
    # ```

    def reverse_list(the_list):
        print("Los elementos de la lista en orden inverso son: ")

        list_length = len(the_list)
        recorrido = range(list_length - 1, -1, -1)

        for i in recorrido:
            print(the_list[i])

    list1 = [5, 4, 3, 2, 1]
    list2 = ["C", "B", "A"]

    reverse_list(list1)
    reverse_list(list2)

    print()

    # 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

    def capitalize_list_items_comprehension(the_list):
        return [str(item).capitalize() for item in the_list]

    my_list = ["river", "plate", "juani", "gancio", 9]
    print(
        f"Lista escrita con mayúsculas utilizando comprensión de listas: {capitalize_list_items_comprehension(my_list)}"
    )

    def capitalize_list_items_classical(the_list):
        new_list = list()
        for i in the_list:
            new_list.append(str(i).capitalize())

        return new_list

    print(
        f"""Lista escrita con mayúsculas de manera "tradicional": {capitalize_list_items_classical(my_list)}"""
    )

    # Bonus: Voy a probar usar la función map() para conseguir el mismo resultado.

    def capitalize_list_items_map(the_list):
        new_list = list(map(lambda items: str(items).capitalize(), the_list))
        return new_list

    print(
        f"""Lista escrita con mayúsculas utilizando la función "map" {capitalize_list_items_map(my_list)}"""
    )

    print()

    # 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

    # ```py
    # food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    # print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
    # numbers = [2, 3, 7, 9]
    # print(add_item(numbers, 5))      [t2, 3, 7, 9, 5]
    # ```

    def add_item(the_list, new_item):
        # No modifico la lista original, por ello voy a realizar una copia para guardar la lista acutalizada con el nuevo elemento.
        new_list = the_list.copy()
        new_list.append(new_item)
        return new_list

    food_staff = ["Potato", "Tomato", "Mango", "Milk"]
    numbers = [2, 3, 7, 9]

    print(add_item(food_staff, "Meat"))
    print(add_item(numbers, 5))

    print()

    # 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

    # ```py
    # food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    # print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
    # numbers = [2, 3, 7, 9]
    # print(remove_item(numbers, 3))  # [2, 7, 9]
    # ```

    def remove_item(the_list, item_to_delete):
        new_list = the_list.copy()
        new_list.remove(item_to_delete)
        return new_list

    print(remove_item(food_staff, "Mango"))
    print(remove_item(numbers, 3))

    print()

    # 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

    # ```py
    # print(sum_of_numbers(5))  # 15
    # print(sum_of_numbers(10)) # 55
    # print(sum_of_numbers(100)) # 5050
    # ```

    def sum_of_numbers(the_number):
        sum = 0
        for i in range(1, the_number + 1, 1):
            sum += i

        return sum

    print(sum_of_numbers(5))
    print(sum_of_numbers(10))
    print(sum_of_numbers(100))

    print()

    def sum_of_numbers_recursive(the_number):
        if the_number == 0:
            return 0
        else:
            return the_number + sum_of_numbers_recursive(the_number - 1)

    print(sum_of_numbers_recursive(5))
    print(sum_of_numbers_recursive(10))
    print(sum_of_numbers_recursive(100))

    print()

    def sum_of_numbers_math(the_number):
        return the_number * (the_number + 1) // 2  # Fórmula de Gauss

    print(sum_of_numbers_math(5))
    print(sum_of_numbers_math(10))
    print(sum_of_numbers_math(100))

    print()

    # 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

    def sum_of_odds(the_number):
        odd_list = [number for number in range(0, the_number + 1, 1) if number % 2 != 0]

        sum = 0

        for number in odd_list:
            sum += number

        return sum

    print(sum_of_odds(10))

    def sum_of_odds_with_sum(the_number):
        return sum(range(1, the_number + 1, 2))

    print(sum_of_odds_with_sum(10))

    print()

    # 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.

    def sum_of_even(the_number):
        even_list = [number for number in range(0, the_number + 1, 2)]

        return sum(even_list)

    print(sum_of_even(10))

    def sum_of_even_with_sum(the_number):
        return sum(range(0, the_number + 1, 2))

    print(sum_of_even_with_sum(10))

    def sum_of_even_comprehension(the_number):
        even_list = [number for number in range(the_number + 1) if number % 2 == 0]
        return sum(even_list)

    print(sum_of_even_comprehension(10))

    def sum_of_even_filter(the_number):
        the_list = list(range(the_number + 1))
        even_list = list(filter(lambda number: number % 2 == 0, the_list))
        return sum(even_list)

    print(sum_of_even_filter(10))

    def sum_of_even_traditional(the_number):
        total = 0
        for number in range(0, the_number + 1, 2):
            total = total + number

        return total

    print(sum_of_even_traditional(10))


if __name__ == "__main__":
    d11_level1()
