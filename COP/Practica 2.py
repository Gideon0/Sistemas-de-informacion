!pip install ortools

#Primer ejercicio
solver = pywraplp.Solver.CreateSolver("GLOP")

A = solver.NumVar(0, solver.infinity(), name="A")
B = solver.NumVar(0, solver.infinity(), name="B")

c_mezcla = solver.Add(2*A + 4*B <= 11, name="mezcla")
c_pigmentación = solver.Add(3*A + B <= 9, name="pigmentación")

solver.Maximize(6*A + 2.1*B)

tipo_resultado = solver.Solve()

if tipo_resultado == solver.ABNORMAL :
  print("Se ha producido un error mientras se ejecutaba el solver")
elif tipo_resultado == solver.FEASIBLE :
  print("Se ha encontrado una solución factible")
  print("Valor para la variable", A.name(), 'es de', A.solution_value())
  print("Valor para la variable", B.name(), 'es de', B.solution_value())
  print("El valor de la solución es de", solver.Objective().Value())
elif tipo_resultado == solver.INFEASIBLE :
  print("El problema no tiene solución posible")
elif tipo_resultado == solver.NOT_SOLVED :
  print("No se ha podido encontrar ninguna solución en el tiempo proporcionado")
elif tipo_resultado == solver.OPTIMAL :
  print("Ha encontrado la solución óptima")
  print("Valor para la variable", A.name(), 'es de', A.solution_value())
  print("Valor para la variable", B.name(), 'es de', B.solution_value())
  print("El valor de la solución es de", solver.Objective().Value())
  print("Se han requerido un total de ", solver.Iterations(), "iteraciones del algoritmo para su resolución")
elif tipo_resultado == solver.UNBOUNDED :
  print("Solución no acotada por las restricciones")
else :
  print("Código de error desconocido")

#Problema 1: Plan de inversion de marketing
from ortools.linear_solver import pywraplp

#Creación de la instancia del solver
solver = pywraplp.Solver.CreateSolver('GLOP')

#Creación de las variables de decisión
SM = solver.NumVar(0, solver.infinity(), name="Social Media")
TV = solver.NumVar(0, solver.infinity(), name="Television")
INFL = solver.NumVar(0, solver.infinity(), name="Influencer")


#Creación de las restricciones del problema
c_inversion = solver.Add(SM >= 200, name="inversion SM")
c_presupuesto = solver.Add(SM + TV + INFL <= 2000, name="presupuesto maximo")
c_diferencia = solver.Add(INFL - TV <= 500, name="diferencia")

#Creación de la función objetivo
solver.Maximize(1.5*SM + 1.3*TV + 2.1*INFL)

#Resolución del problema e interpretación del resultado
tipo_resultado = solver.Solve()

if tipo_resultado == solver.ABNORMAL :
  print("Se ha producido un error mientras se ejecutaba el solver")
elif tipo_resultado == solver.FEASIBLE :
  print("Se ha encontrado una solución factible")
  print("Valor para la variable", SM.name(), 'es de', SM.solution_value())
  print("Valor para la variable", TV.name(), 'es de', TV.solution_value())
  print("Valor para la variable", INFL.name(), 'es de', INFL.solution_value())
  print("El valor de la solución es de", solver.Objective().Value())
elif tipo_resultado == solver.INFEASIBLE :
  print("El problema no tiene solución posible")
elif tipo_resultado == solver.NOT_SOLVED :
  print("No se ha podido encontrar ninguna solución en el tiempo proporcionado")
elif tipo_resultado == solver.OPTIMAL :
  print("Ha encontrado la solución óptima")
  print("Valor para la variable", SM.name(), 'es de', SM.solution_value())
  print("Valor para la variable", TV.name(), 'es de', TV.solution_value())
  print("Valor para la variable", INFL.name(), 'es de', INFL.solution_value())
  print("El valor de la solución es de", solver.Objective().Value())
  print("Se han requerido un total de ", solver.Iterations(), "iteraciones del algoritmo para su resolución")
elif tipo_resultado == solver.UNBOUNDED :
  print("Solución no acotada por las restricciones")
else :
  print("Código de error desconocido")

#Problema 2: Mezclado en construccion 
from ortools.linear_solver import pywraplp

#Creación de la instancia del solver
solver = pywraplp.Solver.CreateSolver('GLOP')

#Creación de las variables de decisión
M1 = solver.NumVar(0, solver.infinity(), name="maquina 1")
M2 = solver.NumVar(0, solver.infinity(), name="maquina 2")


#Creación de las restricciones del problema
c_arena = solver.Add(M1*0.3 + M2*0.6 >= 5000, name="cantidad de arena")
c_grava = solver.Add(M1*0.7 + M2*0.4 <= 6000, name="cantidad de grava")
c_total = solver.Add(M1 + M2 >= 10000)


#Creación de la función objetivo
solver.Minimize(M1 * 5 + M2 * 7)

#Resolución del problema e interpretación del resultado
tipo_resultado = solver.Solve()

if tipo_resultado == solver.ABNORMAL :
  print("Se ha producido un error mientras se ejecutaba el solver")
elif tipo_resultado == solver.FEASIBLE :
  print("Se ha encontrado una solución factible")
  print("Valor para la variable", M1.name(), 'es de', M1.solution_value())
  print("Valor para la variable", M2.name(), 'es de', M2.solution_value())
  print("El valor de la solución es de", solver.Objective().Value())
elif tipo_resultado == solver.INFEASIBLE :
  print("El problema no tiene solución posible")
elif tipo_resultado == solver.NOT_SOLVED :
  print("No se ha podido encontrar ninguna solución en el tiempo proporcionado")
elif tipo_resultado == solver.OPTIMAL :
  print("Ha encontrado la solución óptima")
  print("Valor para la variable", M1.name(), 'es de', M1.solution_value())
  print("Valor para la variable", M2.name(), 'es de', M2.solution_value())
  print("El valor de la solución es de", solver.Objective().Value())
  print("Se han requerido un total de ", solver.Iterations(), "iteraciones del algoritmo para su resolución")
elif tipo_resultado == solver.UNBOUNDED :
  print("Solución no acotada por las restricciones")
else :
  print("Código de error desconocido")

#Problema 3: Un plan de gasto en la nube
from ortools.linear_solver import pywraplp
#Creación de la instancia del solver
solver = pywraplp.Solver.CreateSolver('GLOP')

#Creación de las variables de decisión
MB_S1 = solver.NumVar(0, solver.infinity(), name="MB software 1")
MB_S2 = solver.NumVar(0, solver.infinity(), name="MB software 2")
H_S1 = solver.NumVar(0, solver.infinity(), name="Tiempo software 1")
H_S2 = solver.NumVar(0, solver.infinity(), name="Tiempo software 2")

#Creación de las restricciones del problema
c_MBS1 = solver.Add(MB_S1 >= (10 * 3600), name="minimo MB s1")
c_MBS2 = solver.Add(MB_S2 >= (5 * 3600), name="minimo MB s2")
c_HS1 = solver.Add(H_S1 >= 600, name="minimo horas s1")
c_HS2 = solver.Add(H_S2 >= 300, name="minimo horas s2")
c_relacionMB = solver.Add(MB_S2 >= 3*MB_S1 , name="relacion MB de uso")
c_relacionHoras = solver.Add(H_S2 >= 2*H_S1, name="relacion horas de uso")
c_presupuesto = solver.Add(0.01*(MB_S1+MB_S2) + 0.05*(H_S1+H_S2) <= 1500, name="presupuesto")

#Creación de la función objetivo
solver.Minimize(0.01*(MB_S1+MB_S2) + 0.05*(H_S1+H_S2))

#Resolución del problema e interpretación del resultado
tipo_resultado = solver.Solve()

if tipo_resultado == solver.ABNORMAL :
  print("Se ha producido un error mientras se ejecutaba el solver")
elif tipo_resultado == solver.FEASIBLE :
  print("Se ha encontrado una solución factible")
  print("Valor para la variable", MB_S1.name(), 'es de', MB_S1.solution_value())
  print("Valor para la variable", MB_S2.name(), 'es de', MB_S2.solution_value())
  print("Valor para la variable", H_S1.name(), 'es de', H_S1.solution_value())
  print("Valor para la variable", H_S2.name(), 'es de', H_S2.solution_value())
  print("El valor de la solución es de", solver.Objective().Value())
elif tipo_resultado == solver.INFEASIBLE :
  print("El problema no tiene solución posible")
elif tipo_resultado == solver.NOT_SOLVED :
  print("No se ha podido encontrar ninguna solución en el tiempo proporcionado")
elif tipo_resultado == solver.OPTIMAL :
  print("Ha encontrado la solución óptima")
  print("Valor para la variable", MB_S1.name(), 'es de', MB_S1.solution_value())
  print("Valor para la variable", MB_S2.name(), 'es de', MB_S2.solution_value())
  print("Valor para la variable", H_S1.name(), 'es de', H_S1.solution_value())
  print("Valor para la variable", H_S2.name(), 'es de', H_S2.solution_value())
  print("El valor de la solución es de", solver.Objective().Value())
  print("Se han requerido un total de ", solver.Iterations(), "iteraciones del algoritmo para su resolución")
elif tipo_resultado == solver.UNBOUNDED :
  print("Solución no acotada por las restricciones")
else :
  print("Código de error desconocido")