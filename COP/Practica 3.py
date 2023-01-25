#De esta practica el codigo no es correcto
#Te servira como una guia para resolver la practica

#Tarea 1

# Tu código aquí
import time 
import numpy

lista_media = []
lista_std = []
for i in range(100, 1001, 100):
  lista = []
  for j in range(1, 31, 1):
    (variables, constraints, o, solver) = generate_random_lp_problem(i, 100)
    t1 = time.time()
    result_type = solver.Solve()
    t2 = time.time()
    t_total = t2 - t1
    lista.append(t_total)
  lista_media.append(average(lista))
  lista_std.append(std(lista))

# Tu código aquí
import matplotlib.pyplot as plt
lista_var = (range(100,1001,100))
x = lista_var
y = lista_media
errores = lista_std

fig= plt.errorbar(x,y, yerr=errores)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Ejemplo de gráfica")
plt.legend( ["serie 1"] )

#Tarea 2

#Tu código aquí
import time 
import numpy

lista_media = []
lista_std = []
for i in range(100, 1001, 100):
  lista = []
  for j in range(1, 31, 1):
    (variables, constraints, o, solver)  = generate_random_lp_problem(100, i)
    t1 = time.time()
    result_type = solver.Solve()
    t2 = time.time()
    t_total = t2 - t1
    lista.append(t_total)
  lista_media.append(average(lista))
  lista_std.append(std(lista))

# Tu código aquí
import matplotlib.pyplot as plt
lista_var = (range(100,1001,100))
x = lista_var
y = lista_media
errores = lista_std

fig= plt.errorbar(x,y, yerr=errores)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Ejemplo de gráfica")
plt.legend( ["serie 1"] )

#Tarea 3

#Tu código aquí
import time 
import numpy

lista_media = []
lista_std = []
for i in range(100, 1001, 100):
  lista = []
  for j in range(1, 31, 1):
    (variables, constraints, o, solver) = generate_random_lp_problem(i, i//2)
    t1 = time.time()
    result_type = solver.Solve()
    t2 = time.time()
    t_total = t2 - t1
    lista.append(t_total)
  lista_media.append(average(lista))
  lista_std.append(std(lista))

#Tu código aquí
import matplotlib.pyplot as plt
lista_var = (range(100,1001,100))
x = lista_var
y = lista_media
errores = lista_std

fig= plt.errorbar(x,y, yerr=errores)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Ejemplo de gráfica")
plt.legend( ["serie 1"] )

#Tarea 4

#Tu código aquí
import time 
import numpy

lista_media1 = []
lista_std1 = []
lista_media2 = []
lista_std2 = []

for i in range(500, 3501, 500):
  lista1 = []
  lista2 = []
  for j in range(1, 11, 1):
    v1,v2,v3,_= generate_random_lp_problem(i, i//2)
    t1 = time.time()
    result_type = solver.Solve()
    t2 = time.time()
    t_total1 = t2 - t1
    lista1.append(t_total1)

    copy_problem(v1, v2, v3)
    t3 = time.time()
    result_type = solver.Solve()
    t4 = time.time()
    t_total2 = t4 - t3
    lista2.append(t_total2)
  lista_media1.append(average(lista1))
  lista_std1.append(std(lista1))
  lista_media2.append(average(lista2))
  lista_std2.append(std(lista2))

#Tu código aquí
from matplotlib import pyplot as plt
lista_var = (range(1000,3001,500))
x = lista_var
x2 = lista_var
y = lista_media1
y2 = lista_media2
errores = lista_std1
errores2 = lista_std2

fig= plt.errorbar(x,y, yerr=errores)
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Ejemplo de gráfica")
plt.subplot()
plt.errorbar(x2,y2, yerr=errores2)
plt.legend( ["serie 1", "serie 2"] )
