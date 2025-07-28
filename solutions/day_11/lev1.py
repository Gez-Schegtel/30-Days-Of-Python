def d11_level1():
    print("\n### Ejercicios: Día 11, nivel 1. ###\n")

    # 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.

    def add_two_numbers(n1, n2):
        return n1 + n2

    print(f"Utilizando una función tradicional: {add_two_numbers(6, 4)}")

    add_two_numbers_lambda = lambda n1, n2: n1 + n2

    print(f"Utilizando una función lambda: {add_two_numbers_lambda(6, 4)}\n")

    # 2. Area of a circle is calculated as follows: area = π × r × r. Write a function that calculates _area_of_circle_.

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

    # 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

    # 6. Write a function called calculate_slope which return the slope of a linear equation

    # 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.

    # 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

    # 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

    # ```py
    # print(reverse_list([1, 2, 3, 4, 5]))
    # # [5, 4, 3, 2, 1]
    # print(reverse_list1(["A", "B", "C"]))
    # # ["C", "B", "A"]
    # ```

    # 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

    # 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

    # ```py
    # food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    # print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
    # numbers = [2, 3, 7, 9]
    # print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
    # ```

    # 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

    # ```py
    # food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    # print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
    # numbers = [2, 3, 7, 9]
    # print(remove_item(numbers, 3))  # [2, 7, 9]
    # ```

    # 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

    # ```py
    # print(sum_of_numbers(5))  # 15
    # print(sum_of_numbers(10)) # 55
    # print(sum_of_numbers(100)) # 5050
    # ```

    # 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

    # 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.


if __name__ == "__main__":
    d11_level1()
