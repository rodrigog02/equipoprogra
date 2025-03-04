# TEAM PADRINOS
#
# ESTE CÓDIGO REALIZA CÁLCULOS DE DERIVADAS DE FUNCIONES SIMBÓLICAS
# UTILIZANDO LA LIBRERÍA SYMPY PARA MATEMÁTICAS SIMBÓLICAS.
# El código permite calcular la derivada de una función simbólica
# con respecto a una variable dada.
#
# 2025 / 03 / 03 - V. 1. 0. 0 - SE AGREGAN COMENTARIOS Y ESTRUCTURA AL CÓDIGO
#
# TRABAJARON: MARIO / LUIGUI Bros

import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

# Función a derivar: en este caso, f(x) = x^2 * sin(x)
f = x**2 * sp.sin(x)

# Calcular la derivada de f(x) con respecto a x
derivada = sp.diff(f, x)
print(f"Derivada de x^2 * sin(x) con respecto a x: {derivada}")

# Derivada de una función de segundo orden (segunda derivada)
segunda_derivada = sp.diff(f, x, 2)
print(f"Segunda derivada de x^2 * sin(x) con respecto a x: {segunda_derivada}")
