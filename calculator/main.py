from src.suma import add

def main():
    while True:
        print("Opciones:")
        print("1. Suma")
        print("5. Salir")

        elección = input("Ingrese su elección (1/5): ")

        if elección == '5':
            print("¡Adiós!")
            break

        if elección in ('1'):
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))

                if elección == '1':
                    print("Resultado:", add(num1, num2))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos.")
        else:
            print("Elección no válida. Por favor, ingrese una opción válida (1/5).")

if __name__ == "__main__":
    main()