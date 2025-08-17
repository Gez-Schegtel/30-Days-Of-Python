def d11_level2():
    print("\n### Ejercicios: Día 11, nivel 2. ###\n")

    # 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    # print(evens_and_odds(100))
    ## The number of odds are 50.
    ## The number of evens are 51.

    def evens_and_odds(the_number):
        blizzard_of_oddz = 0
        blizzard_of_evens = 0

        for i in range(0, the_number + 1, 1):
            if i % 2 != 0:
                blizzard_of_oddz += 1
            else:
                blizzard_of_evens += 1

        print(f"Number of odds are {blizzard_of_oddz}")
        print(f"Number of evens are {blizzard_of_evens}")

    evens_and_odds(100)

    print()

    # 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

    def factorial(the_number):
        fact = 1
        for i in range(1, the_number + 1):
            fact *= i

        print(f"{the_number}! = {fact}")

    factorial(6)

    print()

    # 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not

    def is_empty(something_in_the_way) -> bool:
        return not bool(something_in_the_way)

    test_var = []
    print(f"¿La variable {test_var} está vacía? -> {is_empty(test_var)}")

    test_var = (1, 2, 2, 3)
    print(f"¿La variable {test_var} está vacía? -> {is_empty(test_var)}")

    print()

    # 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

    my_list = [3, 6, 7, 8, 9, 15, 2]

    def calculate_mean_traditional(the_list):
        return sum(the_list) / len(the_list)

    print(
        f"El promedio de la lista {my_list} es {calculate_mean_traditional(my_list)}."
    )

    from statistics import mean

    def calculate_mean(the_list):
        return mean(the_list)

    print(f"El promedio de la lista {my_list} es {calculate_mean(my_list)}.")

    def calculate_median_traditional(the_list):
        new_list = the_list.copy()
        sorted_list = sorted(new_list)
        list_length = len(sorted_list)

        if list_length % 2 == 0:
            return (
                sorted_list[(list_length - 1) // 2] + sorted_list[list_length // 2]
            ) / 2
        else:
            return sorted_list[list_length // 2]

    print(
        f"La media de la lista {sorted(my_list)} es {calculate_median_traditional(my_list)}."
    )

    from statistics import median

    def calculate_median(the_list):
        return median(the_list)

    print(f"La media de la lista {sorted(my_list)} es {calculate_median(my_list)}.")

    from statistics import mode

    def calculate_mode(the_list):
        return mode(the_list)

    my_list.extend([9, 9, 9, 9, 9])
    print(f"La moda de la lista {sorted(my_list)} es {calculate_mode(my_list)}.")

    def calculate_range(the_list):
        return max(the_list) - min(the_list)

    print(f"El rango de la lista {my_list} es {calculate_range(my_list)}.")

    from statistics import variance

    def calculate_variance(the_list):
        return variance(the_list)

    print(f"La varianza de la lista {my_list} es {calculate_variance(my_list)}.")

    from statistics import stdev

    def calculate_stdev(the_list):
        return stdev(the_list)

    print(f"El desvío estándar de la lista {my_list} es {calculate_stdev(my_list)}.")


if __name__ == "__main__":
    d11_level2()
