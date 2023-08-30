from src.suma import add
from src.resta import subtract
from src.multiplicacion import multiply
from src.division import divide

def main():
    while True:
        print("Opciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        elección = input("Ingrese su elección (1/2/3/4/5): ")

        if elección == '5':
            print("¡Adiós!")
            break

        if elección in ('1','2','3','4'):
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))

                if elección == '1':
                    print("Resultado:", add(num1, num2))
                elif elección == '2':
                    print("Resultado:", subtract(num1, num2))
                elif elección == '3':
                    print("Resultado:", multiply(num1, num2))
                elif elección == '4':
                    print("Resultado:", divide(num1, num2))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos.")
        else:
            print("Elección no válida. Por favor, ingrese una opción válida (1/2/3/4/5).")

if __name__ == "__main__":
    main()