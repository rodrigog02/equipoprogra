# TEAM PADRINOS
#
# ESTE CÓDIGO REALIZA CÁLCULOS DE INTEGRALES DEFINIDAS E INDEFINIDAS
# USANDO LA LIBRERÍA SYMPY PARA MATEMÁTICAS SIMBÓLICAS.
# El código permite calcular tanto la integral indefinida como la definida
# de una función simbólica y muestra los resultados.
#
# 2025 / 03 / 03 - V. 1. 0. 0 - SE AGREGAN COMENTARIOS Y ESTRUCTURA AL CÓDIGO
#
# TRABAJARON: MARIO / LUIGUI Bros

import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

# Función a integrar: en este caso, f(x) = sin(x) * exp(x)
f = sp.sin(x) * sp.exp(x)

# Calcular la integral indefinida de la función f(x)
integral_indefinida = sp.integrate(f, x)
print(f"Integral indefinida de sin(x) * exp(x): {integral_indefinida}")

# Calcular la integral definida de la función f(x) en el intervalo [0, pi]
integral_definida = sp.integrate(f, (x, 0, sp.pi))
print(f"Integral definida de sin(x) * exp(x) de 0 a pi: {integral_definida}")

