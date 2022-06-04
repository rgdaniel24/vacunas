import matplotlib.pyplot as plt
import numpy as np



def leer_numero_empleados():
  print("Recuerde que si no ingresa un número mayor a 0, el código le generara error")
  nun = int(input("Ingresa el número de empleados: "))
  #num2 = leer_numero_empleados
  return nun

def leer_ventas_empleados_mes():
  num = leer_numero_empleados()
  matriz = []

  for i in range(num):
    nombre = input("Ingresa el nombre del vacunador: ")
    ene = int(input("Ingresa las vacunas del mes de Enero: " ))
    feb = int(input("Ingresa las vacunas del mes de Febrero: "))
    mar = int(input("Ingresa las vacunas del mes de Marzo: "))
    abr = int(input("Ingresa las vacunas del mes de Abril: "))
    may = int(input("Ingresa las vacunas del mes de Mayo: " ))
    jun = int(input("Ingresa las vacunas del mes de Junio: "))
    jul = int(input("Ingresa las vacunas del mes de Julio: "))
    ago = int(input("Ingresa las vacunas del mes de Agosto: "))
    sep = int(input("Ingresa las vacunas del mes de Septiembre: "))
    oct = int(input("Ingresa las vacunas del mes de Octubre: "))
    nov = int(input("Ingresa las vacunas del mes de Noviembre: "))
    dic = int(input("Ingresa las vacunas del mes de Diciembre: "))
    matriz.append([nombre, ene, feb, mar, abr, may, jun, jul, ago, sep, oct, nov, dic])

   
  return matriz

def ordenar_vendedores_por_ventas(matriz):
  con=0
  lis=[]
  for i in range(0,len(matriz)):
    for j in range(1,13):
      con+=matriz[i][j]
    lis.append(con)
    con=0
  lisf = []
  lis1 = list(reversed(sorted(lis)))
  lisnom = []
  for i in range(0, len(lis)):
    ind = lis.index(lis1[i])
    lisnom.append(matriz[ind][0])
    lisf.append(lis[ind])
    lis[ind]=-1
  print("El orden de los vacunadores de acuerdo al número de vacunados es: ")
  for i in range(0, len(lis)):
    print("El vacudanor", lisnom[i], "vacuno en el año a", lisf[i], "personas")
  return [lisnom, lisf]
  


def calcular_cinco_vendedores(matriz):
  matriz_5 = [[],[]]
  for i in range(5):
    matriz_5[0].append(matriz[0][i])
    matriz_5[1].append(matriz[1][i])
  return matriz_5
    

def calcular_mes_mas_ventas(matriz):
  con = 0
  lis=[]
  for i in range(1,13):
    for j in range(0,len(matriz)):
      con+=matriz[j][i]
    lis.append(con)
    
  
  

def greficar_ventas_por_mes(lismes):
  meses = ['Enero', 'Febrero', 'Marzo','Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
  fig, ax = plt.subplost()
  ax.set_ylabel('Vacunas totales')
  ax.set_title('Meses')
  plt.bar(meses, lismes)
  plt.show()


#4

#print(list(reversed(sorted([25,26,23,1,5,456,2,85,3]))))
hj = ordenar_vendedores_por_ventas(leer_ventas_empleados_mes())
print("los cinco mejores vendedores son: ", calcular_cinco_vendedores(hj)[0])