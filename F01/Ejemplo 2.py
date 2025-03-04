# Importamos la librería sympy para trabajar con matemáticas simbólicas
import sympy as sp

# Definimos la variable simbólica
x = sp.symbols('x')

# Definimos la función que vamos a integrar
f = x**2 + 3*x + 2  # Por ejemplo, f(x) = x^2 + 3x + 2

# Definimos los límites de integración
a = 0  # Límite inferior
b = 2  # Límite superior

# Calculamos la integral definida de f(x) desde a hasta b
integral = sp.integrate(f, (x, a, b))

# Imprimimos el resultado
print(f"La integral definida de {f} desde {a} hasta {b} es: {integral}")

