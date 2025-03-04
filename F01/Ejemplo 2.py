import sympy as sp

# Definir la variable
x = sp.symbols('x')

# Función a integrar
f = sp.sin(x) * sp.exp(x)

# Integral indefinida
integral_indefinida = sp.integrate(f, x)
print(f"Integral indefinida de sin(x) * exp(x): {integral_indefinida}")

# Integral definida en un intervalo, por ejemplo de 0 a pi
integral_definida = sp.integrate(f, (x, 0, sp.pi))
print(f"Integral definida de sin(x) * exp(x) de 0 a pi: {integral_definida}")
