# Solicita al usuario que ingrese un número y lo convierte a entero
numero = int(input("Ingrese un número: "))

# Verifica si el número es par o impar
if numero % 2 == 0:
    # Si el residuo de la división entre 2 es 0, imprime que el número es par
    print("El número es par")
else:
    # Si el residuo no es 0, imprime que el número es impar
    print("El número es impar")
