"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
total = 0
bloques_superan_70 = 0
for asistencia in asistencias:
    total= total + asistencia
    if asistencia > capacidad * 0.7:
        bloques_superan_70 = bloques_superan_70 + 1
        
# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = total / len(asistencias)
porcentaje_ocupacion = (promedio / capacidad) * 100

# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if porcentaje_ocupacion >= 80:
    estado = "Ocupación alta"
elif porcentaje_ocupacion >= 50:
    estado = "Ocupación media"
else:
    estado = "Ocupación baja"

# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
print(f"Total de asistentes: {total}", 
      f"\nPromedio de asistentes: {promedio:.0f}", 
      f"\nPorcentaje de ocupación: {porcentaje_ocupacion:.0f} %", 
      f"\nCantidad de bloques que superan el 70 %: {bloques_superan_70}", 
      f"\nEstado del promedio: {estado}")
