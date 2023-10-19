
Vscode Extension

algebra lineal usando python


python
Download
Copy code
import sympy as sp

# Solución general del sistema de ecuaciones lineales
def solve_linear_system(equations):
   symbols = sp.symbols('x y')
   solution = sp.solve(equations, symbols)
   return solution

# Sistema de ecuaciones lineales dado
equation1 = sp.Eq(3*sp.symbols('x') + 2*sp.symbols('y'), 9)
equation2 = sp.Eq(sp.symbols('x') - sp.symbols('y'), 1)

# Solución del sistema de ecuaciones lineales
solution = solve_linear_system([equation1, equation2])
print("La solución del sistema de ecuaciones lineales es:", solution)
