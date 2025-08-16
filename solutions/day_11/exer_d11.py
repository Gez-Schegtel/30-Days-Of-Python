# 💻 Exercises: Day 11

from lev1 import d11_level1
from lev2 import d11_level2
from lev3 import d11_level3

VALID_OPTIONS = ("0", "1", "2", "3")


def show_menu() -> None:
    print("\n🎓 Menú De Ejercicios")
    print("1 - Nivel 1")
    print("2 - Nivel 2")
    print("3 - Nivel 3")
    print("0 - Salir")


def option_selection() -> str:
    show_menu()

    while True:
        user_option = input(">> ")

        if user_option in VALID_OPTIONS:
            break

        print(f"¡Error! Las opciones correctas son: {'/'.join(VALID_OPTIONS)}\n")

    return user_option


def main():
    while True:
        selected_option = option_selection()

        match selected_option:
            case "1":
                d11_level1()
            case "2":
                d11_level2()
            case "3":
                d11_level3()
            case "0":
                print("\n¡Hasta luego!\n")
                break


if __name__ == "__main__":
    main()
