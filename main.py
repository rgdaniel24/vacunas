import vacunas as vt
import numpy as np

# Caso omiso a esta matriz
#mimatriz= [["Juan", 1, 3, 4, 2, 1, 5, 7, 2, 1, 4, 3, 6],['Stuart', 4, 1, 3, 5, 7, 9, 3, 3, 7, 9, 10, 2]]

print("Datos de vacunación")
matriz=vt.leer_ventas_empleados_mes()
print(np.array(matriz))
lisnom=vt.ordenar_vendedores_por_ventas(matriz)
cinco_mejores= vt.calcular_cinco_vendedores(matriz)
lismes=vt.calcular_mes_mas_ventas(matriz)
print(lismes)
vt.graficar_ventas_por_mes(lismes)
