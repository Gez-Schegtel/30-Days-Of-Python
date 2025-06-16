def d10_level1():
    print("\nEstos son los ejercicios del día 10, nivel 1.")

    # ==============================
    #       Exercises: Level 1
    # ==============================

    # 1. Iterate from 0 to 10 using a for loop. Do the same using a while loop.
    print("Punto 1:")

    for _ in range(0, 11):
        print(f"For loop iteration n.° {_}")

    print()

    # 2. Iterate from 10 to 0 using a for loop. Do the same using a while loop.
    print("Punto 2:")

    control_var = 0
    while 0 <= control_var <= 10:
        print(f"While loop iteration n.° {control_var}")
        control_var += 1

    print()

    # 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
    #    #
    #    ##
    #    ###
    #    ####
    #    #####
    #    ######
    #    #######
    print("Punto 3:")

    print("Versión 1: ")

    output_text = "#"

    for _ in range(0, 7):
        print(output_text)
        output_text = output_text + "#"

    print("\nVersión 2:")

    for i in range(1, 8):
        print("#" * i)

    print()

    # 4. Use nested loops to create the following pattern:
    #    # # # # # # # #
    #    # # # # # # # #
    #    # # # # # # # #
    #    # # # # # # # #
    #    # # # # # # # #
    #    # # # # # # # #
    #    # # # # # # # #
    #    # # # # # # # #

    print("Punto 4: ")

    print("Versión 1: ")

    # Usamos un bucle externo para las filas
    for _ in range(8):
        # Bucle interno para las columnas
        for _ in range(8):
            print("#", end=" ")
        print()  # Salto de línea después de cada fila

    print("\n Versión 2: ")

    for _ in range(0, 8):
        output_text = ""

        for _ in range(0, 8):
            output_text = "# " + output_text

        print(output_text)

    print()

    # 5. Print the following multiplication pattern:
    # 0 x 0 = 0
    # 1 x 1 = 1
    # 2 x 2 = 4
    # 3 x 3 = 9
    # 4 x 4 = 16
    # 5 x 5 = 25
    # 6 x 6 = 36
    # 7 x 7 = 49
    # 8 x 8 = 64
    # 9 x 9 = 81
    # 10 x 10 = 100

    print("Punto 5: ")

    for i in range(11):
        print(f"{i} × {i} = {i * i}")

    # 6. Iterate through the list ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print each item.

    # 7. Use a for loop to iterate from 0 to 100 and print only even numbers.

    # 8. Use a for loop to iterate from 0 to 100 and print only odd numbers.


if __name__ == "__main__":
    # Este condicional simple va acá para ejecutar este archivo de código fuente de forma específica si así se lo requiere.
    d10_level1()
