def d10_level2():
    print("\nEstos son los ejercicios del día 10, nivel 2.\n")

    # ==============================
    #       Exercises: Level 2
    # ==============================

    # 1. Use a for loop to iterate from 0 to 100 and print the sum of all numbers.
    #    Output: The sum of all numbers is 5050.

    print("Punto 1:")
    acuml = 0
    for number in range(101):
        acuml = acuml + number

    print(f"La suma de todos los números es: {acuml}")

    print()

    # 2. Use a for loop to iterate from 0 to 100 and print:
    #    - The sum of all evens
    #    - The sum of all odds
    #    Output: The sum of all evens is 2550. And the sum of all odds is 2500.

    print("Punto 2:")

    acuml_evens = 0
    acuml_odds = 0

    for number in range(0, 101):
        if number % 2 == 0:
            acuml_evens += number
        else:
            acuml_odds += number

    print(f"La suma de todos los números pares es: {acuml_evens}")
    print(f"La suma de todos los números impares es: {acuml_odds}\n")


if __name__ == "__main__":
    # Este condicional simple va acá para ejecutar este archivo de código fuente de forma específica si así se lo requiere.
    d10_level2()
