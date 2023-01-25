#Planificador de dietas optimas

  # Tu código aquí
import requests
r = requests.get('https://gitlab.com/drvicsana/cop-practicas-upv/-/raw/master/data/food.json')
food_db = list( r.json().values() )

r = requests.get('https://gitlab.com/drvicsana/cop-practicas-upv/-/raw/master/data/food_requirements.json')
food_requirements = r.json()

print(food_db[19])
print(food_db[4]['name'])
print(food_db[99]['price'])

food3 = food_db[2]['nutrients']
nutrientes_totales = 0
for nutri in food3:
  nutrientes_totales = nutrientes_totales + nutri['amount']
print('Nutrientes totales de la tercera comida:', nutrientes_totales)

food2 = food_db[1]['nutrients']
print('Nombre del ultimo nutriente:', food2[-1]['nutrient_name'])

name_quinto = food_requirements[4]['nutrient_name']
print(name_quinto)

#Solver
from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("GLOP")

# Variables
lista_alimentos = []
for alimento in food_db:
  food = solver.NumVar(0, solver.infinity(), "Cantidad de " + alimento['name'])
  lista_alimentos.append(food)

#Funcion objetivo
objetivo = solver.Objective()
z = None
for i in range(len(lista_alimentos)):
  precio_alimento = food_db[i]['price']
  alimento = lista_alimentos[i]
  if z: 
    z = z + precio_alimento * alimento
  else: 
    z = precio_alimento * alimento
solver.Minimize(z)

#Restricciones
lista_restricciones = []
for requerimiento in food_requirements: 
  if('lb' in requerimiento):
    if('ub' in requerimiento):
      c = solver.Constraint(requerimiento['lb'], requerimiento['ub'], "Cantidad de " + requerimiento['nutrient_name'])
    else:
      c = solver.Constraint(requerimiento['lb'], solver.infinity(), "Cantidad de " + requerimiento['nutrient_name'])
  else:
    c = solver.Constraint(0, requerimiento['ub'], "Cantidad de " + requerimiento['nutrient_name'])

  for i in range(len(lista_alimentos)):
    v = lista_alimentos[i]
    food = food_db[i]
    for nutrientes in food['nutrients']:
       if requerimiento['nutrient_id'] == nutrientes['nutrient_id']:
         cant_nutriente = nutrientes['amount']
         c.SetCoefficient(v, cant_nutriente) 
  lista_restricciones.append(c)

#Resolucion del modelo
result = solver.Solve()
print("Solucion óptima: ",objetivo.Value())
for v in lista_alimentos: 
  if v.SolutionValue() != 0: 
    print(v.name(), ":", v.SolutionValue())