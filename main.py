import vacunas as vt
import numpy as np

print("Datos de vacunación")
num = vt.leer_numero_empleados()
matriz=vt.leer_ventas_empleados_mes()
print(np.array(matriz))
lisnom=vt.ordenar_vendeores_por_ventas(matriz)
vt.calcular_cinco_vendedores(lisnom,num)
vt.visualizar_matriz()
lismes=vt.calcula_mes_mas_ventas(matriz)
vt.greficar_ventas_por_mes(lismes)

